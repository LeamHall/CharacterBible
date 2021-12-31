#!/usr/bin/env perl

# name:     get_character.pl
# version:  0.2.1
# date:     20201121
# author:   Leam Hall
# desc:     Get a character by a limited parameter set.

use strict;
use warnings;

use DBI;
use File::Basename;
use Getopt::Long;

use lib "lib";
use DataMine;

my $sth;
my $return;
my $dbfile;
my $dbf;
my $dbh;
my $column;
my $like;
my $table;
my $query   = "SELECT * from ";
my $help    = 0;
my $datamine;

GetOptions(
  "c=s"   => \$column,
  "d=s"   => \$dbf,
  "l=s"   => \$like,
  "t=s"   => \$table,
  "h"     => \$help,
);

if ( $help ) {
  print "Usage: get_character.pl \n";
  print "\t -c <column> \n";
  print "\t -d <database file> \n";
  print "\t -l <field LIKE>    '%' are acceptable \n";
  print "\t -t <table> \n";
  print "\t -h                 This menu \n";
  exit;
}

if ( $dbf ) {
  $dbfile = $dbf;
} else {
  $dbfile = 'tmp/data/people.db';
}

if ( -f $dbfile ) {
  $datamine    = DataMine->new( type => 'sqlite', file => $dbfile );
} else {
  die "Can't find $dbfile: $!";
}

# Use this to get the column header names, for 
# later checking.
# Note that this does not work with multiple tables, yet.
#$sth      = $dbh->prepare( "SELECT * from $table;" );
#$return   = $sth->execute() or die "$DBI::errstr";
#if ( $return < 0 ) {
#  print $DBI::errstr;
#}
#my $fields_ref  = $sth->{NAME};
#my @fields      = values @$fields_ref;
#my %fields      = map { $_ => 1 } @fields;

sub show_character {
  my %data  = %{$_[0]};
  my $rank        = $data{rank}         || '';
  my $last_name   = $data{last_name}    || '';
  my $first_name  = $data{first_name}   || '';
  my $gender      = $data{gender}       || '';
  my $notes       = $data{notes}        || '';
  my $str         = $data{str}          || 0;
  my $dex         = $data{dex}          || 0;
  my $end         = $data{end}          || 0;
  my $int         = $data{int}          || 0;
  my $edu         = $data{edu}          || 0;
  my $soc         = $data{soc}          || 0;
  my $psr         = $data{psr}          || 0;
  my $plot        = $data{plot}         || '';
  my $temperament = $data{temperament}  || '';
  my %skills      = %{ $data{skills}    || {} };
  my $upp         = sprintf "%X%X%X%X%X%X", $str, $dex, $end, $int, $edu, $soc;
  my $line;
  $line           .= "$rank " if $rank;
  $line           .= "$first_name $last_name [$upp] $gender\n";
  my $skill_line  = '';
  foreach my $skill ( sort (keys %skills) ) {
    $skill_line   .= ", " if $skill_line;
    my $level     = $skills{$skill};
    $skill_line   .= "$skill-$level";
  }
  $line           .= "$skill_line\n" if $skill_line;
  $line           .= "Plot: $plot \n" if $plot;
  $line           .= "Temperament: $temperament \n" if $temperament;
  $line           .= "Notes: $notes" if $notes;
  $line           .= "\n"; 
  print $line;
}

my  @results      = $datamine->search_2d6ogl( $column, $like );
my $result_count = scalar(@results);
foreach  my $row ( @results) {
  my %data            = %$row;
  # Yes, it is intentional to set the formerly INTEGER value to a TEXT field.  :)
  $data{plot}         = $datamine->search_by_id( 'plot', 'plots', $data{plot} );
  $data{temperament}  = $datamine->search_by_id( 'temperament', 'temperaments', $data{temperament} );
  $data{skills}       = $datamine->get_person_skills( $data{id} );
  print "---\n";
  show_character(\%data);
  print "\n";
}



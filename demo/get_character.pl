#!/usr/bin/env perl

# get_character.pl
# version:  0.1.0
# date:     20201111
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
  $dbh     = DBI->connect("dbi:SQLite:dbname=$dbfile", "", "");
} else {
  die "Can't find $dbfile: $!";
}

if ( $table ) {
  $query  .= "$table ";
} else {
  # Assumes the table requested is the same as the filename.
  # Likely a poor assumption.
  my ($filename)  = fileparse($dbfile);
  ( $table = $filename ) =~ s/\.db//;
  $query          .= "$table ";
}

# Use this to get the column header names, for 
# later checking.
# Note that this does not work with multiple tables, yet.
$sth      = $dbh->prepare( "SELECT * from $table;" );
$return   = $sth->execute() or die "$DBI::errstr";
if ( $return < 0 ) {
  print $DBI::errstr;
}
my $fields_ref  = $sth->{NAME};
my @fields      = values @$fields_ref;
my %fields      = map { $_ => 1 } @fields;

my $s4_query  = "select people.last_name, people.first_name, people.gender, people.notes, ";
$s4_query     .= "chars_2d6ogl.* FROM people INNER JOIN chars_2d6ogl ON people.id = chars_2d6ogl.people_id ";

# Needs better error checking.
if ( $column && $like ) {
  #$fields{$column} or die "There is no $column column";
  $s4_query  .= "WHERE $column LIKE '$like' ";
} 

# Finalize the query.
$s4_query  .= ";";

sub show_character {
  my ( $last_name, $first_name, $gender, $notes, $id,
    $str, $dex, $end, $int, $edu, $soc, $psr,) = @_;
  $last_name  = $last_name  || '';
  $first_name = $first_name || '';
  $gender     = $gender     || '';
  $notes      = $notes      || '';
  $str        = $str        || 0;
  $dex        = $dex        || 0;
  $end        = $end        || 0;
  $int        = $int        || 0;
  $edu        = $edu        || 0;
  $soc        = $soc        || 0;
  $psr        = $psr        || 0;
  my $upp     = sprintf "%X%X%X%X%X%X", $str, $dex, $end, $int, $edu, $soc;
  my $line  = "$first_name $last_name [$upp] $gender\n";
  $line     .= $notes;
  $line     .= "\n"; 
  print $line;
}

#$sth          = $dbh->prepare( $s4_query );
#$return       = $sth->execute() or die "$DBI::errstr";
#if ( $return < 0 ) {
#  print $DBI::errstr;
#}

print "dbfile is $dbfile.\n";
my $datamine    = DataMine->new( type => 'sqlite', file => $dbfile );
my $results_ref = $datamine->search();
my @results     = \$results_ref;
#while ( my @row = $sth->fetchrow_array()) {
foreach  my $row ( @results) {
  print "---\n";
  show_character($row);
  print "\n";
}

$dbh->disconnect();


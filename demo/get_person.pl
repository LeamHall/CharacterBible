#!/usr/bin/env perl

# get_person.pl
# version:  0.0.1
# date:     20201111
# author:   Leam Hall
# desc:     Get a person by a limited parameter set.

use strict;
use warnings;

use DBI;
use File::Basename;
use Getopt::Long;

my $sth;
my $return;
my $dbfile  = 'data/people.db';
my $dbf;
my $dbh;
my $column;
my $like;
my $table;
my $query   = "SELECT * from ";
my $help    = 0;
my $verbose = 0;

GetOptions(
  "c=s"   => \$column,
  "d=s"   => \$dbf,
  "l=s"   => \$like,
  "t=s"   => \$table,
  "v"     => \$verbose,
  "h"     => \$help,
);

if ( $help ) {
  print "Usage: get_character.pl \n";
  print "\t -c <column> \n";
  print "\t -d <database file> \n";
  print "\t -l <field LIKE>    '%' are acceptable \n";
  print "\t -t <table> \n";
  print "\t -v                 Verbose response \n";
  print "\t -h                 This menu \n";
  exit;
}


if ( $dbf ) {
  $dbfile = $dbf;
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
$sth      = $dbh->prepare( "SELECT * from $table;" );
$return   = $sth->execute() or die "$DBI::errstr";
if ( $return < 0 ) {
  print $DBI::errstr;
}
my $fields_ref  = $sth->{NAME};
my @fields      = values @$fields_ref;
my %fields      = map { $_ => 1 } @fields;

if ( $column && $like ) {
  $fields{$column} or die "There is no $column column";
  $query  .= "WHERE $column LIKE '$like' ";
} 

# Finalize the query.
$query  .= ";";

sub show_character {
  my ( $id, $last_name, $first_name, $middle_name, $suffix_name, $other_name, 
    $gender, $birthdate, $plot, $temperament, $notes ) = @_;
  $last_name    = $last_name    || '';
  $first_name   = $first_name   || '';
  $middle_name  = $middle_name  || '';
  $suffix_name  = $suffix_name  || '';
  $other_name   = $other_name   || '';
  $gender       = $gender       || '';
  $birthdate    = $birthdate    || '';
  $plot         = $plot         || '';
  $temperament  = $temperament  || '';
  $notes        = $notes        || '';

  my $line      = "$first_name $last_name [$gender] Birthdate: $birthdate\n";
  $line         .= "Plot: $plot \n";
  $line         .= "Temperament: $temperament \n";
  $line         .= "Notes: $notes \n";
  if ( $verbose ){
    $line       .= "ID: $id \n";
  }
  print $line;
}

$sth      = $dbh->prepare( $query );
$return   = $sth->execute() or die "$DBI::errstr";
if ( $return < 0 ) {
  print $DBI::errstr;
}

while ( my @row = $sth->fetchrow_array()) {
  print "---\n";
  show_character(@row);
  print "\n";
}

$dbh->disconnect();


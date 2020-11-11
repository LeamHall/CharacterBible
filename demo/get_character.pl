#!/usr/bin/env perl

# get_character.pl
# version:  0.0.1
# date:     20201106
# author:   Leam Hall
# desc:     Get a character by a limited parameter set.

use strict;
use warnings;

use DBI;
use File::Basename;
use Getopt::Long;

my $sth;
my $return;
my $dbfile  = 'tmp/data/cadets.db';
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
  $dbfile = 'tmp/data/cadets.db';
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
  my ( $year, $cadre, $id, $last_name, $first_name, $gender, 
    $upp, $birth_year, $birth_day, $notes) = @_;
  my $line  = "$first_name $last_name [$upp] $gender\n";
  $line     .= $notes;
  $line     .= "\n"; 
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


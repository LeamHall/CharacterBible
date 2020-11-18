#!/usr/bin/env perl

# update_person.pl
# version:  0.0.1
# date:     20201118
# author:   Leam Hall
# desc:     Update data in the people database.

use strict;
use warnings;

use DBI;
use File::Basename;
use Getopt::Long;

use lib "lib";
use DataMine;

my $sth;
my $return;
my $dbfile  = 'tmp/data/people.db';
my $dbf;
my $dbh;
my $id;
my $column;
my $value;
my $table;
my $query   = "SELECT * from ";
my $help    = 0;
my $datamine;

GetOptions(
  "c=s"   => \$column,
  "d=s"   => \$dbf,
  "v=s"   => \$value,
  "i=i"   => \$id,
  "t=s"   => \$table,
  "h"     => \$help,
);

if ( $help ) {
  print "Usage: get_character.pl \n";
  print "\t -c <column> \n";
  print "\t -d <database file> \n";
  print "\t -i <id>  \n";
  print "\t -v <value>    \n";
  print "\t -t <table> \n";
  print "\t -h                 This menu \n";
  exit;
}

if ( $dbf ) {
  $dbfile = $dbf;
} else {
  # Why is this duplicated?
  $dbfile = 'tmp/data/people.db';
}

if ( -f $dbfile ) {
  $datamine = DataMine->new( type => 'sqlite', file => $dbfile );
} else {
  die "Can't find $dbfile: $!";
}

unless ( $id and $column ) {
  die "Must have an id and a column";
}

my %data = ( id => $id, column => $column, value => $value );
$datamine->update_person(\%data);


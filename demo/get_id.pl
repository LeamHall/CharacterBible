#!/usr/bin/env perl

# get_id.pl
# version:  0.0.1
# date:     20201118
# author:   Leam Hall
# desc:     Get a person's ID by a limited parameter set.

use strict;
use warnings;

use DBI;
use File::Basename;
use Getopt::Long;

use lib "lib";
use DataMine;

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
}

if ( -f $dbfile ) {
  $datamine = DataMine->new( type => 'sqlite', file => $dbfile );
  #DBI->connect("dbi:SQLite:dbname=$dbfile", "", "");
} else {
  die "Can't find $dbfile: $!";
}

sub show_character {
  my %data          = %{$_[0]};
  my $id            = $data{id}           || '';
  my $last_name     = $data{last_name}    || '';
  my $first_name    = $data{first_name}   || '';
  my $gender        = $data{gender}       || '';
  my $birthdate     = $data{birthdate}    || '';

  my $line      = "$id $first_name $last_name [$gender] Birthdate: $birthdate\n";
  print $line;
}

my @results     = $datamine->search_people( $column, $like );
my $result_count  = scalar(@results);
foreach my $row ( @results ) {
  print "---\n";
  show_character($row);
  print "\n";
}



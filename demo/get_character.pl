#!/usr/bin/env perl

# get_character.pl
# version:  0.0.1
# date:     20201106
# author:   Leam Hall
# desc:     Get a character by a limited parameter set.

use strict;
use warnings;

use DBI;
my $dbfile  = 'tmp/data/cadets.db';
my $dbh;
if ( -f $dbfile ) {
  $dbh     = DBI->connect("dbi:SQLite:dbname=$dbfile", "", "");
} else {
  die "Can't find $dbfile: $!";
}

my $sth     = $dbh->prepare("SELECT * FROM cadets WHERE last_name LIKE 'Domici';");
my $return  = $sth->execute() or die "$DBI::errstr";
if ( $return < 0 ) {
  print $DBI::errstr;
}

while ( my @row = $sth->fetchrow_array()) {
  print "$row[4] $row[3] has a birthday on $row[8].\n";
}

$dbh->disconnect();



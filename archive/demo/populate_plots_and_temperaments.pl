#!/usr/bin/env perl

# name:     populate_columns.pl
# version:  0.0.1
# date:     20201121
# author:   Leam Hall
# desc:     Update a table with semi-random data.

use strict;
use warnings;
use File::Basename;
use Getopt::Long;

my $table;
my $max_plots         = 43;
my $max_temperaments  = 15;
my $max_people        = 123;
my $sql_file;

my $program = basename( $0 );

sub usage {
  my $line  = "Usage: $program";
  $line     .= "  -table <table>";
  $line     .= "  -sql_file <sql_file>";
  print $line, "\n";
  exit;
}
   
GetOptions(
  "table=s"     => \$table,
  "sql_file=s"  => \$sql_file,
);

( $table and $sql_file ) or usage();
open( my $sql_fh, '>', $sql_file) or die "Can't open $sql_file: $!";

select $sql_fh;
print "BEGIN DEFERRED;\n";
my $person_id       = 1;
while ( $person_id  <= $max_people ) {
  my $plot          = int( rand( $max_plots ))         + 1;
  my $temperament   = int( rand( $max_temperaments ))  + 1;
  print "UPDATE $table SET plot = $plot, temperament = $temperament WHERE id = $person_id;\n";
  $person_id        += 1;
}
print "END;\n";

close( $sql_fh );


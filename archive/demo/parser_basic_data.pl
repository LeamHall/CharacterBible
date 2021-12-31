#!/usr/bin/env perl

# name:     parser_basic_data.pl
# version:  0.0.1
# date:     20201121
# author:   Leam Hall
# desc:     Parse a text file and build an SQL file.

use strict;
use warnings;
use File::Basename;
use Getopt::Long;

my $data_file;
my $sql_file;
my $column;
my $table;
my $program = basename( $0 );

sub usage {
  my $line  = "Usage: $program";
  $line     .= "  -data_file <data_file>";
  $line     .= "  -sql_file <sql_file>";
  $line     .= "  -column <column>";
  $line     .= "  -table <table>";
  print $line, "\n";
  exit;
}
   
GetOptions(
  "data_file=s" => \$data_file,
  "sql_file=s"  => \$sql_file,
  "column=s"    => \$column,
  "table=s"     => \$table,
);

( $column and $table and $data_file and $sql_file ) or usage();
open( my $data_fh, $data_file) or die "Can't open $data_file: $!";
open( my $sql_fh, '>', $sql_file) or die "Can't open $sql_file: $!";

select $sql_fh;
print "BEGIN DEFERRED;\n";
foreach my $datum ( readline( $data_fh )) {
  next if $datum =~ m/^#/;
  chomp $datum;
  print "INSERT INTO $table ($column) VALUES ( '$datum' );\n";
}
print "END;\n";

close( $sql_fh );
close( $data_fh );


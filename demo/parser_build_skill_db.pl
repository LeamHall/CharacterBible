#!/usr/bin/env perl

# name:     parser_build_skill_db.pl
# version:  0.0.1
# date:     20201119
# author:   Leam Hall
# desc:     Parse skill list and build a SQL file.

use strict;
use warnings;

my $skill_file  = 'skills.txt';
open( my $skill_fh, $skill_file) or die "Can't open $skill_file: $!";

my $sql_file    = 'skills_add.sql';
open( my $sql_fh, '>', $sql_file) or die "Can't open $sql_file: $!";

select $sql_fh;
print "BEGIN DEFERRED;\n";
foreach my $skill ( readline( $skill_fh )) {
  chomp $skill;
  print "INSERT INTO skills (skill) VALUES ( '$skill' );\n";
}
print "END;\n";

close( $sql_fh );
close( $skill_fh );


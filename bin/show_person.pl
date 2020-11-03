#!/usr/bin/env perl

# show_person.pl
# Mostly to check on things I'm learning.

use strict;
use warnings;

use lib "lib";
use Person;

my @data = ( 'Al', 20 );
my $p = Person->new(@data);
my %stat_data = ( str => 7, dex => 7, end => 10, int => 6, edu => 5, soc => 11 ) ;
$p->set_stats(%stat_data);
$p->set_stat('str', 8);

use Data::Dumper;
my $data = $p->{_stat_data};
my %data = %{$data};
print Dumper($data), ".\n";


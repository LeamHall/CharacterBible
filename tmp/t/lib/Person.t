# t/Person.t

use strict;
use warnings;
use lib "lib";
use Person;

use Test::More;

use_ok( 'Person' ) or die $!;

my %data = ( first_name => 'Al', last_name => 'Lefron' );
my $p = Person->new(%data);

isa_ok($p, 'Person');
is($p->name, 'Al Lefron');

my %stat_data = ( str => 7 );
$p->set_stats(%stat_data);
is($p->stat_data('str'), 7);

$p->set_stat('str', 8);
is($p->stat_data('str'), 8);


done_testing();

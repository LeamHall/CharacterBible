# t/lib/Character_2d6.t

use strict;
use warnings;
use lib "lib";
use Person;
use Character_2d6;

use Test::More;

use_ok('Character_2d6') or die "$!";

my $person  = Person->new("Al Lefron", 20);
my %stats   = ( str => 8, end => 10, dex => 7, int => 6, edu => 10, soc => 12 );
my $char    = Character_2d6->new($person);
$char->set_stats(%stats);
is($char->get_upp, '87A6AC');

$char->add_skill('CbtR', 2);
is($char->get_skill('CbtR'), 2);

done_testing();


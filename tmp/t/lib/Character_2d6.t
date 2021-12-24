# t/lib/Character_2d6.t

use strict;
use warnings;
use lib "lib";
use Person;
use Character_2d6;

use Test::More;

use_ok('Character_2d6') or die "$!";

#my %person_data = ( last_name => "Lefron", first_name => "Al" );
# Need to work on the data structure stuff.
my $person  = Person->new();
my %stats   = ( str => 8, end => 10, dex => 7, int => 5, edu => 5, soc => 12 );
my $char    = Character_2d6->new($person);
$char->set_stats(%stats);
is($char->upp_str, '87A55C');

$char->add_skill('CbtR', 2);
is($char->get_skill('CbtR'), 2);

$char->add_skill('ZeroG', 2);
is($char->get_skill('ZeroG'), 2);

$char->add_skill('Kissing', 0);
$char->add_skill('Blade', 2);
is($char->skill_str(), 'Blade-2, CbtR-2, Kissing-0, ZeroG-2');

done_testing();


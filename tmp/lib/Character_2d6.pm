# Character_2d6

package Character_2d6;

use strict;
use warnings;

=encoding utf8

=head1 Character_2d6 Provides characters for 2d6 skill based games.
=cut

=over 4

=item new
  Requires a person object.
  
    my $person  = Person->new( first_name => "Al", last_name => "Lefron");
    my $char    = Character_2d6->new($person);
=cut
sub new {
  my ($class) = @_;
  bless {
    person   => $_[1],
  }, $class;
}

=item upp_str
  Returns the UPP as a string

    $char->upp_str;
=cut
sub upp_str {
  my $self = shift;
  my $upp_str = '';
  foreach my $stat ( qw( str dex end int edu soc ) ) {
    $upp_str .= sprintf("%X", $self->{person}->stat_data($stat) );
  }
  return $upp_str;
}

=item set_stats
  Requires a hash, sets the stats accordingly.

    my %stats   = ( str => 8, end => 10, dex => 7, int => 6, edu => 10, soc => 12 );
    $char->set_stats(%stats);
=cut
sub set_stats {
  my ($self, %stats) = @_;
  $self->{person}->set_stats(%stats);  
}

=item add_skill
  Requires a skill (hash key) and a value.

    $char->add_skill('CbtR', 2);
=cut
sub add_skill {
  my ($self, $skill, $level) = @_;
  $self->{skills}{$skill} += $level;
}

=item get_skill
  Requires a skill, returns the value for that skill.

  $char->get_skill('CbtR');
=cut
sub get_skill {
  my ($self, $skill) = @_;
  return $self->{skills}{$skill};
}

=item skill_str
  Returns an alpha sorted comma and space seperated skill list.

  $char->skill_str();
=cut
sub skill_str {
  my ($self)    = @_;
  my $skill_str = '';
  my @skills    = keys %{$self->{skills}};
  @skills       = sort(@skills);
  foreach my $skill ( @skills ) {
    if ( length($skill_str) > 0 ) {
      $skill_str .= ", ";
    }
    $skill_str  .= "$skill-$self->{skills}->{$skill}";
  }
  return $skill_str;
}
=back
=cut


1;

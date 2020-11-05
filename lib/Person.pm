package Person;

use strict;
use warnings;

=encoding utf8

=head1 Person contains the common factors for all characters

=cut

=over 4

=item new
  Requires a "name" (string) and an age (number)

    my $person = Person->new( name => 'Al Lefron', age => 20);
=cut

sub new {
  #my ($class) = @_;
  #bless {
  #  _name       => $_[1],
  #  _age        => $_[2],
  #  stat_data  => undef,
  #}, $class;
  my ($class, %args) = @_;
  bless \%args, $class;
}

=item age
  Returns the age.
=cut
sub age     { $_[0]->{age} };


=item name
  Returns the person's name.
=cut
sub name    { $_[0]->{name} };


=item set_stat
  Requires a stat and a value.

    $person->set_stat('str', 8);
=cut
sub set_stat  { 
  my ($self, $stat, $value) = @_;
  $self->{stat_data}{$stat} = $value;
}


=item set_stats
  Requires a hash, usually with stat, values as key/value pairs.

    my %stats   = ( str => 8, end => 10, dex => 7, int => 6, edu => 10, soc => 12 );    
    $person->set_stats(%stats);
=cut
sub set_stats { 
  my ($self, %stats) = @_;
  %{$self->{stat_data}} = %stats;
}


=item stat_data
  Requires a stat (key), returns the value for that stat

    $person->stat_data('str');
=cut
sub stat_data {
  my ($self, $stat) = @_;
  return $self->{stat_data}{$stat};
}

=back
=cut

1;

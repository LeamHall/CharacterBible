# name:     DataMine.pm
# version:  0.0.1
# date:     20201114
# author:   Leam Hall
# desc:     Provide an adapter to get data from sources.

package DataMine;

use strict;
use warnings;

=encoding utf8

=head1  SYNOPSIS

  DataMine provides the interface between requests and sources.

=head1  DESCRIPTION

  An Adapter object. Requires a data source type and file.

  my $datamine = DataMine->new( type => 'sqlite', file => 'data/my_data.db' );
=cut

sub new {
  # Needs a way to validate the type, and test for the file.
  my ( $class, %args ) = @_;
  bless \%args, $class;
}

sub file { $_[0]->{file} };

sub search {
  my ($self)  = shift;
  my ($column, $like )  = @_;
  my $dbfile  = $self->file;
  my $dbh     = DBI->connect("dbi:SQLite:dbname=$dbfile", "", "") or die "Can't open $dbfile: $!";
 
  my $query   = qq{
    SELECT people.last_name, people.first_name, people.gender, people.notes, chars_2d6ogl.*
    FROM people INNER JOIN chars_2d6ogl ON people.id = chars_2d6ogl.people_id
  };
  if ( $column and $like ) {
    print "column is $column and like is $like.\n";
    $query .= qq{ WHERE ? LIKE ? };
    #return $dbh->selectall_array( $query, { Slice => {} }, ( $column, $like ) );
    return $dbh->selectall_array( $query, { Slice => {} }, ( 'last_name', 'Lefron' ) );
  } else {
    return $dbh->selectall_array( $query, { Slice => {} } );
  }
}

1;




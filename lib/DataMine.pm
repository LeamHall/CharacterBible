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

=over 4
=item new

  Takes a hash with keys 'type' (sqlite) and 'file' ( 'tmp/data/people.db').

=cut

sub new {
  # Needs a way to validate the type and test for the file.
  my ( $class, %args ) = @_;
  bless \%args, $class;
}


=item file

  Returns the file name for the database file.
=cut

sub file { $_[0]->{file} };

=item search

  If given a column name and a pattern to match, select those items from the database.
  Return an array of hash references.
=cut

sub search {
  my ($self)  = shift;
  my ($column, $like )  = @_;
  my $dbfile  = $self->file;
  my $dbh     = DBI->connect("dbi:SQLite:dbname=$dbfile", "", "", { RaiseError => 1 }) or die "Can't open $dbfile: $!";
 
  my $query   = qq{
    SELECT people.last_name, people.first_name, people.gender, people.notes, chars_2d6ogl.*
    FROM people INNER JOIN chars_2d6ogl ON people.id = chars_2d6ogl.people_id
  };
  if ( $column and $like ) {
    $query .= qq{ WHERE ${column} LIKE ? };
    return $dbh->selectall_array( $query, { Slice => {} }, $like );
  } else {
    return $dbh->selectall_array( $query, { Slice => {} } );
  }
}

1;


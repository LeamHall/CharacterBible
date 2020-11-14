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
  my ($self)  = @_;
  #my $dbfile  = $self->file;
  my $dbfile  = 'tmp/data/people.db';
  #my $dbh     = DBI->connect("dbi:SQLite:dbname=$self->file", "", "") or die "Can't open $self->file: $!";
  #my $dbh     = DBI->connect("dbi:SQLite:dbname=$dbfile", "", "") or die "Can't open $dbfile: $!";
  my $dbh     = DBI->connect("dbi:SQLite:dbname=$dbfile", "", "") or die "Can't open $dbfile: $!";
  my $column  = 'last_name';
  my $like    = 'Alba';
 
  my $query   = "SELECT people.last_name, people.first_name, people.gender, people.notes, ";
  $query      .= "chars_2d6ogl.* FROM people INNER JOIN chars_2d6ogl ON people.id = chars_2d6ogl.people_id ";
  $query      .= "WHERE $column LIKE '$like' ";
  $query      .= ";";
  my $statement = $dbh->prepare( $query );
  my $return    = $statement->execute() or die "$DBI::errstr";

  my $results   = $statement->fetchall_arrayref;
  $dbh->disconnect();
  return $results;
}

1;




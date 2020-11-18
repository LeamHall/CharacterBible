# name:     DataMine.pm
# version:  0.0.2
# date:     20201118
# author:   Leam Hall
# desc:     Provide an adapter to get data from sources.

# Changelog:
#   20201118  Added search_people (to get IDs), and update_person subs.

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

=item search_people

  If given a column name and a pattern to match, select those items from the people database.
  Returns a limited set of data, keying off the "id" field.
  Return an array of hash references.
=cut

sub search_people {
  my ($self)  = shift;
  my ($column, $like )  = @_;
  my $dbfile  = $self->file;
  my $dbh     = DBI->connect("dbi:SQLite:dbname=$dbfile", "", "", { RaiseError => 1 }) or die "Can't open $dbfile: $!";
 
  my $query   = qq{
    SELECT * from people
  };
  if ( $column and $like ) {
    $query .= qq{ WHERE ${column} LIKE ? };
    return $dbh->selectall_array( $query, { Slice => {} }, $like );
  } else {
    return $dbh->selectall_array( $query, { Slice => {} } );
  }
}

=item update_person

  Requires a hash reference that includes keys for 'id' and 'column'.
  Updates the 'value' for that 'id' and 'column' combination. Defaults to NULL.

=cut

sub update_person {
  # id|last_name|first_name|middle_name|suffix_name|other_name|gender|birthdate|plot|temperament|notes
  my ($self)  = shift;
  my %data    = %{$_[0]};
  my $id      = $data{id};
  my $column  = $data{column};
  my $value   = $data{value}  || 'NULL';
  my $dbfile  = $self->file;
  my $dbh     = DBI->connect("dbi:SQLite:dbname=$dbfile", "", "", { RaiseError => 1 }) or die "Can't open $dbfile: $!";
  my $query   = "UPDATE people SET $column = \"$value\" WHERE id = $id;";
  my $sth     = $dbh->do( $query ) or die $DBI::errstr;
}

1;


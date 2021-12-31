#!/usr/bin/env perl

# parse_characters_cypher.pl

use strict;
use warnings;
use diagnostics;

package Person;

sub new {
  my ($class, %data) = @_;
  my $self = {
    _tag      => $data{tag},
    _name     => $data{name},
    _friends  => [],
    _related  => [],
    _works    => undef,
    _loves    => undef,
    _spouse   => undef,
    _enemy    => [],
    _knows    => [],
  };
  bless $self, $class;
  return $self;
}

sub tag { $_[0]->{_tag} };
sub name { $_[0]->{_name} };

sub add_friend {
  my ( $self, $person ) = @_;
  push ( @{$self->friends}, $person->tag );
}

sub add_related {
  my ( $self, $person ) = @_;
  push ( @{$self->related}, $person->tag );
}

sub friends { $_[0]->{_friends} };
sub related { $_[0]->{_related} };

sub data {
  my $self = shift;
  my $line = "(" . $self->{_tag} . ":Person { name:'" . $self->{_name} . "' })"; 
  return $line;
}

package main;

my %characters;
my $char_file_name = 'characters_cypher.txt';
open my $char_file, '<', $char_file_name or die "Can't open $char_file_name: $!";
while (<$char_file>) {
  chomp;
  my @char      = split(/\s+/, $_);
  my %data;
  my $char_tag  = shift(@char);
  my $char_name = join(" ", @char);
  my $person    = Person->new(
    tag  => $char_tag,
    name => $char_name,
  );
  $characters{$person->tag} = $person;
}
close($char_file);

foreach my $char ( keys(%characters) ) {
  print "CREATE ". $characters{$char}->data . ";\n";
}

# match (rob:Person {name:"Rob"}) match (oldw:Person {name:"Old Winnie" }) create (rob)-[rel:IS_RELATED_TO]->(oldw)
my $rel_file_name = 'relationships_cypher.txt';
open my $rel_file, '<', $rel_file_name or die "Can't open $rel_file_name: $!";
while( <$rel_file> ) {
  chomp;
  my @rel   = split(/\s+/, $_);
  my $line  = "MATCH ";

  my $rel_tag = 'UNKNOWN';
  $rel_tag  = 'IS_RELATED_TO' if $rel[0]  =~ m/related/;
  $rel_tag  = 'FRIENDS'       if $rel[0]  =~ m/friend/;
  $rel_tag  = 'LOVES'         if $rel[0]  =~ m/love/;
  $rel_tag  = 'WORKS_FOR'     if $rel[0]  =~ m/work/;
  $rel_tag  = 'SPOUSE'        if $rel[0]  =~ m/spouse/;

  my $actor = $characters{$rel[1]};
  my $actee = $characters{$rel[2]};
  $line     .= $actor->data . " MATCH ";
  $line     .= $actee->data . " CREATE (";
  $line     .= $actor->tag  . ")-[rel:" . $rel_tag . "]->(";
  $line     .= $actee->tag  . ");\n";
  print $line;
}
close($rel_file);







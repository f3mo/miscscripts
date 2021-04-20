#!/usr/bin/env perl

#The MIT License (MIT)
#Copyright (c) <year> <copyright holders>

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.j

use strict;
use LWP::Simple;
use HTML::Tree;
use IO::Socket::SSL;

sub parser(){
		my ($url) = @_;
		my $ua = "Mozilla/5.0 (Windows NT 5.1; rv:2.0) Gecko/20100101 Firefox/4.0";
		my $browser = LWP::UserAgent->new();
		my $ag = $browser->agent($ua);
		my $re = $browser->get($url);
		my $page = $re->content;
		return $page;
}
sub get_title(){
		my ($url) = @_;
		my $page = &parser($url);
		my $parse = HTML::Tree->new();
		$parse->parse($page);
		my ($title) = $parse->look_down('_tag','title');
		if (defined $title){
				$title = $title->as_text;
				return $title;
		}
}
if(@ARGV > 4 || @ARGV < 4){
		print "Usage: tbot [NICK] [SERVER] [CHANNEL] [PORT]\n";
		exit;
}
my $user = $ARGV[0];
my $host = $ARGV[1];
my $channel = $ARGV[2];
my $port = $ARGV[3];
my $sock = new IO::Socket::SSL(
		PeerAddr => $host,
		PeerPort => $port,
		Proto => 'tcp',
		SSL_verify_mode => SSL_VERIFY_PEER,
		SSL_ca_path => '/etc/ssl/certs'
) or die "Couldn't connect: $!";
sub reconnect{
		my $sock = new IO::Socket::INET(
				PeerAddr => $host,
				PeerPort => $port,
				Proto => 'tcp',
		) or die "Couldn't connect: $!";
}
sub connect{
		print  $sock "USER $user $user $user :$user IRC\r\n";
		print $sock "NICK $user\r\n";
		print $sock "JOIN $channel\r\n";
}
sub send{
		my ($msg) = @_;
		print $sock "PRIVMSG $channel :\x02\x1Dtitle:\x0F\x0307\x1D $msg\r\n";
}
sub error_code{
		my ($url) = @_;
}
sub join_ch{
		my ($ch) = @_;
		print $sock "JOIN $ch\r\n";
}
&connect;
sub ch_nick{
		my ($ch) = @_;
		print $sock "NICK $ch\r\n";
}
while(1){
		my $line = <$sock>;
		print $line;
		if($line =~ /(PING\s\:\S+)/i){
				my $pg = $1;
				$pg =~ s/PING/PONG/;
				print $sock "$1\r\n";
		}
		if($line =~ /(PRIVMSG\s$channel\s.*)/i){
				if($1 =~ /(http(s)?\S+)/){
						my $url = $1;
						if($url =~ /\.(bin|png|jpeg|jpg|png|gif|webm|gif|pdf|mp4|mp3)/si){
								my $file = "$url | $1";
								#do nothing
						}
						elsif($url =~ /0x0/){

								#do notthing
						}
						else{
								my $title = &get_title($url);
								&send($title);
						}
				}
		}
		if($line =~ /(:Duff_man\S+\sPRIVMSG\s$channel.+)/i){
				my $nick = $1;
				if($nick =~ /(.nick\s\S+)/){
						$nick =~ s/:Duff_man\S+\sPRIVMSG\s$channel\s:\S+\s//;
						print "$nick\n";
						&ch_nick($nick);
		}
		}
		if($line =~ /KICK\s$channel\s$user/){
				sleep 3;
				&connect;
				#prn sc JI canlr\n";
		}
}

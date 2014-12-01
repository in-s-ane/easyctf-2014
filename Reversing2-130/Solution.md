# Solution!

Ok this is not a nice problem. In fact I really hate it due to its sheer stupidity.

Anyways, I was playing around and after a few try you realize that the second input is just a shift key on the string.
Since the final thing should be in English, we can leave the 2nd input blank for now.

So I tried everything from 1 to 150 using the following code:

$ for i in `seq 1 150`;
> do
> echo "$i: " && echo "$i 0" | ./reversing2
> done

And that returned a lot of stuff. Let's skip to the important part:
19:
> > ap text with apostrophes that'll make things a li'l bit harder for you.google 
url shortener code is VfSS0x. here's some cr

Huh, looks like a shifted version of:
here's some crap text with apostrophes that'll make things a li'l bit harder for you.google url shortener code is Vfss0x.

Huh, a google url shortener, so let's check it out, go to goo.gl/VfSS0x.

That redirects to:
http://www.mediafire.com/download/w8g51tyreudc5k0/not+the+flag.rar

Which is a minecraft saved file. Load it up into minecraft and you'll see the file flag.jpg in this directory, and there's your flag!

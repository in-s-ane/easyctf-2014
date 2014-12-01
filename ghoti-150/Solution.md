# Solution!

Ok, few things before we begin, we overcomplicated this, a lot, and I mean A LOT, so yeah, this will contain a rundown of what should be done.

** WHAT SHOULD HAVE BEEN DONE **

We open the corrupted file using bless hex editor or something of that nature, and we run through the thing for possible ascii hints.

Starting at offset 0xe46a, we see this strange ascii text: "here's a hint at the flag: tetraodontidae"

Huh, fascinating, we'll keep that in mind. Then we journey down until we find "FF D9", which marks the EOF of a jpeg file. Huh, after that we see:
Rar!...

Maybe this is another compressed-file-within-picture thing, so we run the following:
$ unrar e ghoti.jpg

That gives us a file called sh58, which contains:
1e95153b6c941098227a4b08d9d74cb9d7b9387f83c74097

Now, ghoti means fish, tetraodontidae is the phylum of blowfish... So this is probably a blowfish cipher.

If you decipher the content of sh58 with the key being tetraodontidae, (you can use anything to help you really, I used http://webnet77.com/cgi-bin/helpers/blowfish.pl)
you get the flag, which is:
bl0w_fish_so_s3cret_

**What we did**

Just for fun, here's how to uncorrupt the image:
At offset 0xed, note how the 12 is weirdly out of place, replace it with an 11, and you get a decent image. Now, take out the here's a hint part, and volia you have the original image

BTW, the original image is this: http://barfblog.com/wp-content/uploads/2012/04/blowfish.jpg
It is from this article: http://barfblog.com/tags/blowfish/

So yeah, you don't need to fix the image.

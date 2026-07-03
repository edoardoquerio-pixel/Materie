# A Method for Obtaining Digital Signatures and Public-Key Cryptosystems

## Panoramica
Signatures and Public-Key Cryptosystems

## Argomenti trattati
Git, API REST, Data Analytics

---
## Appunti

A Method for Obtaining Digital
Signatures and Public-Key Cryptosystems
R.L. Rivest, A. Shamir, and L. Adleman∗
An encryption method is presented with the novel property that publicly revealing an encryption key does not thereby reveal the corresponding decryption
key. This has two important consequences:
1. Couriers or other secure means are not needed to transmit keys, since a
message can be enciphered using an encryption key publicly revealed by
the intended recipient. Only he can decipher the message, since only he
knows the corresponding decryption key.
2. A message can be “signed” using a privately held decryption key. Anyone
can verify this signature using the corresponding publicly revealed encryption key. Signatures cannot be forged, and a signer cannot later deny
the validity of his signature. This has obvious applications in “electronic
mail” and “electronic funds transfer” systems.
A message is encrypted by representing it as a number M, raising M to a
publicly speciﬁed power e, and then taking the remainder when the result is
divided by the publicly speciﬁed product, n, of two large secret prime numbers
p and q. Decryption is similar; only a diﬀerent, secret, power d is used, where
e · d ≡ 1 (mod (p − 1) · (q − 1)). The security of the system rests in part on
the diﬃculty of factoring the published divisor, n.
Key Words and Phrases: digital signatures, public-key cryptosystems, privacy, authentication, security, factorization, prime number, electronic mail,
message-passing, electronic funds transfer, cryptography.
CR Categories: 2.12, 3.15, 3.50, 3.81, 5.25
∗General permission to make fair use in teaching or research of all or part of this material is
granted to individual readers and to nonproﬁt libraries acting for them provided that ACM’s copyright notice is given and that reference is made to the publication, to its date of issue, and to the fact
that reprinting privileges were granted by permission of the Association for Computing Machinery.
To otherwise reprint a ﬁgure, table, other substantial excerpt, or the entire work requires speciﬁc
permission as does republication, or systematic or multiple reproduction.
This research was supported by National Science Foundation grant MCS76-14294, and the Oﬃce of
Naval Research grant number N00014-67-A-0204-0063.
Author’s Address: Laboratory for Computer Science, Massachusetts Institute of Technology, Cambridge, MA 02139 E-mail addresses: rivest@theory.lcs.mit.edu
The era of “electronic mail” [10] may soon be upon us; we must ensure that two
important properties of the current “paper mail” system are preserved: (a) messages
are private, and (b) messages can be signed . We demonstrate in this paper how to
build these capabilities into an electronic mail system.
At the heart of our proposal is a new encryption method. This method provides
an implementation of a “public-key cryptosystem,” an elegant concept invented by
Diﬃe and Hellman [1]. Their article motivated our research, since they presented
the concept but not any practical implementation of such a system. Readers familiar
with [1] may wish to skip directly to Section V for a description of our method.
II Public-Key Cryptosystems
In a “public key cryptosystem” each user places in a public ﬁle an encryption procedure E. That is, the public ﬁle is a directory giving the encryption procedure of each
user. The user keeps secret the details of his corresponding decryption procedure D.
These procedures have the following four properties:
(a) Deciphering the enciphered form of a message M yields M . Formally,
(b) Both E and D are easy to compute.
(c) By publicly revealing E the user does not reveal an easy way to compute D.
This means that in practice only he can decrypt messages encrypted with E, or
compute D eﬃciently.
(d) If a message M is ﬁrst deciphered and then enciphered, M is the result. For-
An encryption (or decryption) procedure typically consists of a general method
and an encryption key. The general method, under control of the key, enciphers a
message M to obtain the enciphered form of the message, called the ciphertext C.
Everyone can use the same general method; the security of a given procedure will rest
on the security of the key. Revealing an encryption algorithm then means revealing
When the user reveals E he reveals a very ineﬃcient method of computing D(C):
testing all possible messages M until one such that E(M ) = C is found. If property
(c) is satisﬁed the number of such messages to test will be so large that this approach
is impractical.
A function E satisfying (a)-(c) is a “trap-door one-way function;” if it also satisﬁes
(d) it is a “trap-door one-way permutation.” Diﬃe and Hellman [1] introduced the
concept of trap-door one-way functions but did not present any examples. These
functions are called “one-way” because they are easy to compute in one direction but
(apparently) very diﬃcult to compute in the other direction. They are called “trapdoor” functions since the inverse functions are in fact easy to compute once certain
private “trap-door” information is known. A trap-door one-way function which also
satisﬁes (d) must be a permutation: every message is the cipertext for some other
message and every ciphertext is itself a permissible message. (The mapping is “oneto-one” and “onto”). Property (d) is needed only to implement “signatures.”
The reader is encouraged to read Diﬃe and Hellman’s excellent article [1] for
further background, for elaboration of the concept of a public-key cryptosystem, and
for a discussion of other problems in the area of cryptography. The ways in which
a public-key cryptosystem can ensure privacy and enable “signatures” (described in
Sections III and IV below) are also due to Diﬃe and Hellman.
For our scenarios we suppose that A and B (also known as Alice and Bob) are
two users of a public-key cryptosystem. We will distinguish their encryption and
decryption procedures with subscripts: EA, DA, EB, DB.
Encryption is the standard means of rendering a communication private. The sender
enciphers each message before transmitting it to the receiver. The receiver (but no
unauthorized person) knows the appropriate deciphering function to apply to the
received message to obtain the original message. An eavesdropper who hears the
transmitted message hears only “garbage” (the ciphertext) which makes no sense to
him since he does not know how to decrypt it.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_A_Method_for_Obtaining_Digital_Signatures_and_Public-Key_Cryptosystems.md*

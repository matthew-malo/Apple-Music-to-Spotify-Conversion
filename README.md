# Apple-Music-to-Spotify-Conversion
Conversion of Apple Music Library to Spotify using Python and Spotipy API

The purpose of this project was to convert my Apple Music Library to Spotify, as I wanted to change music streaming services. 
However, as my library had well over 1000 songs, I figured a fun thing to do would be to automate the transfer while experimenting 
with one of the open source APIs that Spotify lists on their website. This led to a deep dive into the interaction between 
Spotify's API, and the open source community that they promote, and resulted in a neat side project that I used for myself
and offered to friends if they were interested in switching music services as well. 



## Getting Started

The project required a bit of research into both the Spotify API and the Spotipy API that I used in conjunction.
The Spotipy API is very useful, however when I utilized it, it was not very well documented, and some of the functions required 
additional studying to fully understand how to optimally implement them in my code.

Spotify also provides a few useful Javascript files to get the localhost server up and running, which was essential as I had never 
written in Javascript before. The files are very well documented, and provide insight into how to access user data and modify playlists.


## Spotipy API Reference

This is the link to the Spotipy API: https://spotipy.readthedocs.io/en/2.13.0/


### Brief Explination of the API Interaction

Spotify adds songs to playlists via each individual song's URI (uniform resource indicator), which can be accessed via the share menu of any
track, album, or artist profile on Spotify. In order to obtain this URI, Spotipy has an integrated search feature, which returns any and all 
information about the track that is being searched for. This required quite a bit of navigating, which I described more thoroughly in the 
comments on the ObtainURIs python file.

Once obtained, the URIs can be fed to another Spotipy function, which adds each track to a specified playlist on the user's account

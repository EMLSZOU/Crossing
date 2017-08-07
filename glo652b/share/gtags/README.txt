This is a port of GNU GLOBAL to DJGPP v2.03 or later.
GNU GLOBAL is a source code tag system that works the same way across diverse
environments. It supports C, C++, Yacc, Java, PHP4 and assembly source code.

This README file describes how to install GLOBAL on MS-DOS or
MS-Windows systems using the DJGPP port of GNU C/C++ compiler and
development tools.


    1. Unzip the file gloNNNb.zip (where NNN is the version number)
       preserving the directory structure (-d switch to PKUNZIP) from
       the main DJGPP installation directory.  If you will use GLOBAL
       on Windows 9X, use an unzip program which supports long filenames.

    2. If you need to use a custom configuration file, set the
       environment variable:

        GTAGSCONF=%DJDIR%/share/gtags/gtags.conf

       A default gtags.conf is supplied, but not used.

    3. To add an entry to your info directory, assuming you are still
       in the main DJGPP directory:

	install-info share/info/global.info info/dir

       This adds a "GLOBAL" entry to the "Development" section.

    4. Files that begin with "." can also begin with "_".

    5. The plug-in parser is not supported.

    6. The CGI and javascript support files for Htags are not included,
       nor are the server-side scripts.


Jason Hood,
13 June, 2014.

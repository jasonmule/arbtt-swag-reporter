# arbtt-swag-reporter

arbtt2xapi.py sends Arbtt<sup><a id="fnr.1" name="fnr.1" class="footref" href="#fn.1">1</a></sup> reports for a logged in Linux user to a TinCan Learning Record Store.

## Installation<a id="sec-1-2" name="sec-1-2"></a>

    pip install tincan

To run tests:

    pip install nose

You should tag Arbtt entries for output that's more more meaningful e.g

    -- Scratch
    current window $title =~ /.*scratch.*/
            ==> tag Program:Scratch,

will tag all window titles with 'scratch' to `Program:Scratch`

## Configuration
Edit `config.py` to add a Learning Record Store endpoint as well as to map programs to Tincan activities.

## Run the script<a id="sec-1-1" name="sec-1-1"></a>

    arbtt-stats --output-format csv | arbtt2xapi.py

or

    arbtt2xapi.py <arbtt csv file>

assuming that both `arbtt-stats` and `arbtt2xapi.py` are in your path



## Footnotes

<sup><a id="fn.1" name="fn.1" class="footnum" href="#fnr.1">1</a></sup>http://darcs.nomeata.de/arbtt/doc/users_guide

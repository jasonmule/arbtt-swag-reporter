class ArbttRecord:
    """Encapsulates data related to an arbtt csv entry.

    A record will only be created if a valid arbtt csv entry
    is passed. For now, only entries with Program
    tags are allowed and it's possible to configure arbtt
    to tag important captures with the Program prefix e.g.
    
    -- Scratch
    current window $title =~ /.*scratch.*/
        ==> tag Program:Scratch,

    might give you an entry that looks like this:
    Program:Scratch,0:02:00,33.33

    """
    def __init__(self, arbtt_csv_entry):
        self._set_csv_entry(arbtt_csv_entry)
        self._set_application_name(arbtt_csv_entry)
        self._set_app_duration(arbtt_csv_entry)

    def _set_application_name(self, arbtt_csv_entry):
        tag, application = arbtt_csv_entry.split(",")[0].split(":")

        if tag != "Program":
            raise ValueError("Use program tag for Arbtt categories")
        self._application = application

    def _set_csv_entry(self, arbtt_csv_entry):
        length = len(arbtt_csv_entry.split(","))
        if length < 2:
            raise ValueError("csv entry should have at least 2 fields")
        self._csv_entry = arbtt_csv_entry

    def _set_app_duration(self, arbtt_csv_entry):
        duration = arbtt_csv_entry.split(",")[1]

        # Raises ValueError if unpacking fails
        hour, minute, sec = duration.split(":")
        int(hour), int(minute), int(sec)

        self._duration = duration

    @property
    def application(self):
        return self._application

    @property
    def csv_entry(self):
        return self._csv_entry

    @property
    def duration(self):
        return self._duration

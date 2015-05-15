#!/usr/bin/env python
from __future__ import print_function
import os

from config import lrs, activity_map
from arbtt_record import ArbttRecord


from tincan import (
    RemoteLRS,
    Statement,
    Agent,
    Verb,
    Activity,
    ActivityDefinition,
    Extensions,
    Context,
    LanguageMap,
    )

def create_statement(arbtt_csv_entry):
    """Creates a Tincan statement from arbtt csv input"""

    arbtt_record = ArbttRecord(arbtt_csv_entry)
    app = arbtt_record.application
    duration = arbtt_record.duration

    # XXX: Look for a cleaner way to get user details
    user = os.environ['LOGNAME']
    email_address = "%s-arbtt@tunapanda.com" % (user,)
        
    actor = Agent(
        name=user,
        mbox='mailto:'+email_address,
    )

    verb = Verb(
        id='http://adlnet.gov/expapi/verbs/interacted',
        display=LanguageMap({'en-US': 'interacted'}),
    )

    # Get activity from config or set the activity as 'unknown'
    activity_from_map = activity_map.get(app, "unknown")

    object = Activity(
        id=os.path.join(lrs['activities_uri'], activity_from_map),
        definition=ActivityDefinition(
            name=LanguageMap({'en-US': activity_from_map}),
            extensions=Extensions(
                {'http://id.tincanapi.com/extension/duration': duration},
            ),
        ),
    )

    context = Context(
        platform=app
    )

    # Construct the statement
    return Statement(
        actor=actor,
        verb=verb,
        object=object,
        context=context,
    )

if __name__ == '__main__':
    import fileinput
    import sys


    csv_entries = (l.strip() for l in fileinput.input())
    
    remote_lrs = RemoteLRS(
        endpoint=lrs['endpoint'],
        # RemoteLRS uses HTTP Basic Auth
        # so username, password will be sent out
        # with the authorization header.
        username=lrs['username'],
        password=lrs['password'],
    )
    
    for csv_entry in csv_entries:
        try:
            statement = create_statement(csv_entry)
        except ValueError, e:
            # ignore invalid entries
            print("Failed to create statement for %s with the error: %s"
                  % (csv_entry, e), file=sys.stderr)
            continue
        # XXX: Look out for response == None
        # and possibly add the statement to a retry queue
        response = remote_lrs.save_statement(statement)
        if not response.success:
            print("Failed to save statement for %s" % (csv_entry,))

        

    

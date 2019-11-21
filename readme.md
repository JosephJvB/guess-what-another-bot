# Quizbot

Im going to use another slack-client-package (below)

use request.session

reuse http connections

And see if threadcount changes.

I have no idea how important threadcount is.

Threadcount stays low

I guess if I dont reuse http connections,  create new threads up to some default cap (idle threads that dont do anything)

Then when default cap is met, python starts reusing the threads that could have been closed?

My super uneducated guess anyway

CAN also pass session into python-slack slack.webClient(token=token, session=session) except request.Session() doesnt work out of the box, python slack expects a different sessions API which I am not trying to figure out

### also:
- https://github.com/os/slacker: can let me use Requests.Session() to reuse http connection. Maybe that's not more efficient. I dont NEED more efficiency but improvements are improvements so

### Bad design:
1. People liked /whom @user game better
2. Spammy
3. Public reactions means copycats

### Solutions:
1. ?
2. Can delete message of old quiz before win message, and delete win message before new quiz. - Cleanup
3. Copy Slack simple poll app rich embed
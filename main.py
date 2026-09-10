user_choice = None

story = """Jordan is walking home from school when he notices something shining in a storm drain.

He crouches down to get a closer look.

Stuck between the grate bars is a diamond unlike anything he's ever seen.

It seems to pulse faintly, almost like it's breathing.

Jordan reaches for his phone to look it up, but there's no signal here.

He has two options.

A : Reach in and grab the diamond himself.
OR
B : Go find help before touching it.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """Jordan pries the grate loose and pulls the diamond free.

The moment it touches his palm, it gets warmer.

A faint humming fills the air, and the edges of his vision seem to sharpen.

Something has changed, though he can't quite say what it is.

A voice, quiet and unplaceable, seems to whisper from somewhere close by:

"You weren't supposed to find that yet."

A : Ask the voice who it is.
OR
B : Take the diamond and run.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """The voice chuckles, low and amused.

"I'm the one who's been guarding that stone for three hundred years. Congratulations, you're my replacement."

Jordan's stomach drops.

"There are rules," the voice continues. "The diamond can grant one wish. But it also needs a keeper. Forever."

A : Make the wish anyway.
OR
B : Refuse and try to put the diamond back.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """Jordan closes his eyes and wishes for his family to never have to worry about money again.

The diamond flares white-hot, then goes cold and dull in his hand.

The wish is granted, but Jordan feels the weight settle onto his shoulders.

He is the diamond's keeper now, whether he likes it or not.

Some nights, he swears he can hear the next person's footsteps approaching the storm drain.

THE END
"""
            print(story)
        else:
            story = """Jordan drops the diamond back through the grate.

It lands with a soft chime and stops glowing entirely.

The voice sighs, almost sadly.

"Smart. Most people don't say no."

Jordan walks home with nothing but a strange story no one will believe.

THE END
"""
            print(story)

    else:
        story = """Jordan shoves the diamond into his pocket and sprints the rest of the way home.

By the time he gets to his room, the humming has stopped completely.

He sets it on his desk and stares at it for a long time.

It looks like an ordinary, if very large, diamond now.

The next morning, there's a note taped to his window that wasn't there before.

It reads: FOUND YOU.

A : Investigate the note immediately.
OR
B : Hide the diamond somewhere safer first.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """Jordan looks outside and sees nothing but an empty street.

When he turns back, the diamond on his desk is gone.

In its place is a small folded piece of paper.

It simply says: THANK YOU FOR RETURNING IT.

Jordan never does figure out how it got back to wherever it came from.

THE END
"""
            print(story)
        else:
            story = """Jordan buries the diamond in a shoebox at the back of his closet.

Weeks pass and nothing happens, so he almost forgets about it.

Then one afternoon, digging through old clothes, he opens the box to find it's completely empty.

No note, no explanation, just an empty box where a diamond used to be.

THE END
"""
            print(story)

else:
    story = """Jordan decides not to risk it and heads straight to his friend Maya's house instead.

Maya, who reads too many mystery novels for her own good, is immediately thrilled.

"A glowing diamond in a storm drain? Jordan, this is the best thing that's ever happened to you."

Together they walk back, flashlights in hand.

The diamond is exactly where he left it, still pulsing faintly in the dark.

A : Let Maya be the one to grab it.
OR
B : Grab it together at the same time.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """Maya reaches in and lifts the diamond out carefully, like it might bite.

Nothing dramatic happens. No glowing, no voices, just a very heavy, very sparkly rock.

"Well," Maya says, turning it over in her hands, "maybe it's just a diamond."

They take it to a jeweler the next day, half expecting to be laughed out of the shop.

A : Sell the diamond and split the money.
OR
B : Donate it to a museum instead.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The jeweler's eyes go wide the moment he examines it under the loupe.

It turns out to be one of the largest natural diamonds ever found in the region.

Jordan and Maya split the money and, true to their word, remain best friends for life.

THE END
"""
            print(story)
        else:
            story = """The local museum is stunned by the donation and puts the diamond on permanent display.

A small plaque reads: Discovered by Jordan and Maya, age 16.

Years later, kids on school trips still stop to stare at it.

THE END
"""
            print(story)

    else:
        story = """They both grab the diamond at exactly the same moment.

The second their hands touch it together, the humming returns, louder than before.

The storm drain grate begins to glow faintly around the edges.

For a split second, Jordan swears he can see straight through solid concrete, like the whole world has gone slightly transparent.

A : Hold on and see what happens.
OR
B : Let go immediately.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The glow builds and builds, and then, just as suddenly, fades to nothing.

The diamond is warm but otherwise unchanged.

Jordan and Maya look at each other, both certain something important almost happened.

They never do find out what it was, but they never stop wondering either.

THE END
"""
            print(story)
        else:
            story = """They both let go at once, and the diamond drops back into the drain with a hollow clink.

The glow vanishes instantly, like it was never there at all.

Maya laughs nervously. "Yeah, let's just go home."

Some mysteries, they decide, are better left in storm drains.

THE END
"""
            print(story)
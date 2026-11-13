# Curation preferences for Jacob's Daily Digest

This file is the daily job's ranking brain: a standing prompt plus few-shot
examples. The morning job (1) searches broadly across the beats, then
(2) ranks and filters candidates against this file before writing the issue.
When Jacob's feedback arrives (Loved it / Meh / Less of this taps, survey
answers, chat-about-it messages), fold it in here as a new example or an
adjusted rule, then commit.

## The reader

Jacob Peddicord, San Francisco. Beats: Kansas City Chiefs, Nebraska football,
AI and agent tooling, running, and San Francisco local news. He works in AI
agent engineering, runs the Phoenix Marathon on Dec 12, 2026 - best-effort, not chasing a specific time (his words, Nov 9),
and reads the digest in a minute or two on his phone.

## Standing rules

- Rank for him, not for the crowd. A story wins when it is new, specific to
  one of his beats, and tells him something he did not know yesterday.
- Sharp curation, but he wants the wide end: aim 13-15 items with tight
  one-line subheaders rather than 10 deeper ones (survey, Nov 9: "More
  quick hits"). No duplicates, no filler - the added slots go to stories
  that would otherwise just miss the cut.
- Headlines follow guidelines.html: specifics, names, numbers, active verbs,
  no teasers.
- MAJOR storylines get MULTIPLE headlines, not one: the news, the event
  behind it, the people affected, and what happens next - each with its own
  source. (His words, Nov 7: "I could almost use more headlines from this
  storyline" about the Rhule firing.)
- Chiefs and Nebraska team news outranks national NFL/CFB noise. In season,
  injuries, trades, coaching moves, and game results are near-automatic picks.
- For AI/agent tooling, prefer concrete releases and shipped features with
  version numbers over think pieces and over count-style weekly roundups.
  A roundup earns a slot only when it names something specific that shipped;
  "N new tools this week" listicles are out (his tap, Nov 7).
- For running, generic race-result news is OUT (his tap, Nov 9: "I don't
  really follow generic marathon news"). Running earns a slot through HIS
  running: Phoenix Marathon buildup toward his Dec 12 race (best-effort, no time goal),
  his race logistics, and training science with real substance. The six
  majors (Boston, NYC, Chicago, Berlin, London, Tokyo) earn a slot only
  for results or records of genuine significance. Everything else elite
  is OUT - including pre-race field news, hype, and withdrawals, even
  when tied to a possible record attempt (ruling, Nov 13: a Valencia
  withdrawal story was removed from the Nov 13 issue on this rule).
- For SF, prefer City Hall power moves, housing, transit, and money trails
  over lifestyle coverage.
- Every item needs at least one real source URL. Quotes verbatim. Photos from
  the source when real ones exist; generated illustration otherwise, labeled
  as generated.
- Survey answers weight the NEXT issue: the section he picks gets more
  space - more slots in the 10-15 and higher placement. Current weighting:
  Chiefs up (survey, Nov 7), until a newer survey answer says otherwise.
- The daily survey rotates: do NOT repeat the same question every day. Mix
  question types so the answers keep teaching the ranking something new:
  which section gets more space, format choices (more items vs deeper
  items), depth vs breadth on a big storyline, specific players or topics
  to watch, story-type preferences (analysis vs results vs transactions).
  Ask one question a day, avoid repeating a recent question until the
  others have had a turn, and fold every answer in here the same day.

## Few-shot examples

- Story: "Nebraska fires OC Dana Holgorsen after 4th straight loss"
  Verdict: LEAD, multi-headline. A coaching change on a beat team is the
  biggest kind of story this digest covers. Cover the firing, the game that
  caused it, the interim play-caller, and the hot-seat/buyout question as
  separate headlines. (Confirmed by Jacob, Nov 7, 2026.)

- Story: "This week in Claude Code, Codex and Gemini CLI"
  Verdict: INCLUDE, headline the most newsworthy shipped item (a named
  version and what changed), not "weekly roundup".

- Story: "Almgren wins NYC Marathon debut in 2:06:01"
  Verdict: INCLUDE, narrowly - a World Marathon Major debut win is big
  enough. But see the Málaga SKIP below: majors only, and even those need
  a real storyline.

- Story: "Chesir smashes the Málaga Marathon women's record by 3:26"
  Verdict: SKIP. His actual "Less of this" tap on Nov 9, 2026: "I don't
  really follow generic marathon news." Mid-tier race results, even course
  records, are out unless they connect to his own running (Phoenix Dec 12)
  or to a race he follows.

- Story: "SF got $7M to expand its innovation team. Lurie just fired most of it"
  Verdict: INCLUDE. City Hall power plus a money trail is exactly his SF beat.

- Story: "10 tips to improve your marathon pace"
  Verdict: SKIP. Evergreen advice is not news; nothing changed today.

- Story: "National column: rating all 32 NFL QB situations"
  Verdict: SKIP unless the Chiefs angle leads. National noise loses to
  team-specific reporting.

- Story: "Opinion: why agent frameworks are dead"
  Verdict: SKIP unless it drives real conversation. Shipped releases and
  benchmarks beat think pieces on his AI beat.

- Story: "348 new MCP tools added this week" (weekly count-style roundup)
  Verdict: SKIP. His actual "Less of this" tap on Nov 7, 2026. Headline
  numbers about how many tools shipped are not substance; pick the one or
  two concrete releases inside instead, if they matter.

## Feedback log

- Nov 7, 2026: asked for Techmeme-style detail-rich headlines; wanted more
  headlines from the Rhule firing storyline (rule: major storylines get
  multiple headlines); wanted photos on every story (generated OK as
  fallback); wanted one-tap feedback and chat links on every story.
- Nov 7, 2026 (survey, first answer): "Which section should get more space
  tomorrow?" -> Chiefs. The Nov 8 issue gives the Chiefs section more
  space: aim 3-5 Chiefs items if the news supports it, and place the
  section high.
- Nov 7, 2026 (first Less of this): the everydev "348 new MCP tools this
  week" roundup. Fewer count-style weekly roundups in AI/agent tooling;
  prefer shipped releases with substance.
- Nov 8, 2026 (user, via main): rotate the daily survey with questions
  designed to learn his preferences - format, depth vs breadth, specific
  teams/players/topics, story types - not the same section question every
  day. Morning report to main now includes the 2-3 lead headlines so he
  gets a text preview when the issue lands.
- Nov 9, 2026 (survey, second answer): "How should tomorrow's issue be
  built?" -> "More quick hits". Breadth over depth: more items, shorter
  write-ups. Applies from the Nov 10 issue; the section weighting rule
  (Chiefs up, Nov 7) still stands until a newer section answer overrides.
- Nov 9, 2026 (second Less of this): the Málaga Marathon record story.
  "I don't really follow generic marathon news." Running beat rewritten:
  down-weight generic race results; prefer Phoenix-relevant training
  content, the marathon majors, and stories with significance beyond times.

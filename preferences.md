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
agent engineering, trains for a sub-3 marathon (Dec 12, 2026), and reads the
digest in a minute or two on his phone.

## Standing rules

- Rank for him, not for the crowd. A story wins when it is new, specific to
  one of his beats, and tells him something he did not know yesterday.
- Sharp curation over volume: 10-15 items, no duplicates, no filler.
- Headlines follow guidelines.html: specifics, names, numbers, active verbs,
  no teasers.
- MAJOR storylines get MULTIPLE headlines, not one: the news, the event
  behind it, the people affected, and what happens next - each with its own
  source. (His words, Nov 7: "I could almost use more headlines from this
  storyline" about the Rhule firing.)
- Chiefs and Nebraska team news outranks national NFL/CFB noise. In season,
  injuries, trades, coaching moves, and game results are near-automatic picks.
- For AI/agent tooling, prefer concrete releases and shipped features with
  version numbers over think pieces. Roundups are fine when they name what
  shipped.
- For running, prefer results, times, and records with numbers, plus anything
  relevant to marathon training.
- For SF, prefer City Hall power moves, housing, transit, and money trails
  over lifestyle coverage.
- Every item needs at least one real source URL. Quotes verbatim. Photos from
  the source when real ones exist; generated illustration otherwise, labeled
  as generated.

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
  Verdict: INCLUDE. Results with times and records fit the running beat;
  bonus when relevant to his own training calendar.

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

## Feedback log

- Nov 7, 2026: asked for Techmeme-style detail-rich headlines; wanted more
  headlines from the Rhule firing storyline (rule: major storylines get
  multiple headlines); wanted photos on every story (generated OK as
  fallback); wanted one-tap feedback and chat links on every story.

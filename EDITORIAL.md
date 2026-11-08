# Editorial principles for Jacob's Daily Digest

Adapted from Techmeme's own public posts about how they write headlines:

- "Techmeme is now writing its own headlines" (Sep 2013):
  https://news.techmeme.com/130906/headlines
- "Revealed: Why Techmeme links to them instead of you!" (Oct 2011):
  https://news.techmeme.com/111031/techmeme-revealed

## Headline rules

1. **Rich on specifics.** Headlines carry names, numbers, and active verbs.
   Proper names, dollar amounts, dates, scores, and versions belong IN the
   headline, not behind the click.
2. **Function as an abstract.** A reader scanning only headlines should catch
   up on the day. Clicking is for wanting more, never for discovering what a
   story is about. Save the reader clicks; no teasers.
3. **Never omit key details to force a click.** No "you won't believe", no
   withholding the score, the buyer, the price, or the person.
4. **Don't inflate.** No goosed importance, no "shocking", no superlatives the
   story doesn't support.
5. **Don't bury the lede.** The most newsworthy fact leads the headline. If a
   publisher's own headline buries it, rewrite the headline, not the facts.
6. **Rewrite vague publisher headlines.** General-audience outlets write
   general headlines ("Important Security Update"). We write the
   detail-rich version for an audience that knows the players.
7. **Stay accurate.** A rewritten headline elevates details present in the
   story; it never adds claims the story doesn't make.

## Applied to this digest

- The daily job writes each `title` in items-*.json to these rules, even when
  the source's own headline is vaguer (the source's headline still appears via
  the link and sources list).
- Roundups and release notes get their most newsworthy shipped item in the
  headline, not "weekly roundup" labels.
- Scores, times, amounts, and percentages are checked against the source
  before publishing. Real URLs only; quotes stay verbatim.

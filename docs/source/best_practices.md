# Best practices for scientific programming

## Why should we care?

"programs must be written for people to read, and only incidentally for machines to execute”[^1] <div style="text-align: right">—Abelson and others (1996)</div>


“Indeed, the ratio of time spent reading versus writing is well over 10 to 1. We are constantly reading old code as part of the effort to write new code. ...[Therefore,] making it easy to read makes it easier to write.”[^2] <div style="text-align: right">—Robert Martin, in *Clean Code* (2008)</div>

Code is arguably just as much about communication—documenting methods for yourself, your co-workers or collaborators and others—as it is about successfully automating a process. Clean, succinct and readable code can help us work more efficiently, be more productive, and realize the "quality of life" benefits that were one of the motivations for coding in the first place. Messy, unreadable and redundant code takes longer to understand (if we can understand it at all), and can mire us in endless debugging. Work might have to be repeated because of inevitable mistakes. We might be better off just throwing it away and starting over, in which case the communication encapsulated in the original code is lost.

### Technical Debt
For scientists, time lost to bad code might translate to missed deadlines, blown budgets or extra hours. For companies that depend on a reliable codebase to turn a profit, bad code can snowball over time, eventually leading to bankruptcy. Software engineers have a term for this: "[technical debt](https://en.wikipedia.org/wiki/Technical_debt)". In short, expedient solutions and quick fixes to "get it to work" can accelerate code development in the short term, at the cost of slowing development over time by making the code harder to maintain, refactor and extend. The worse the code gets, the less people want to spend time maintaining and improving it.

### Software "Craftsmanship"
As an antidote to this, software engineer and [Agile Manifesto](https://en.wikipedia.org/wiki/Agile_software_development#The_Agile_Manifesto) coauthor Robert Martin argues for software craftsmanship—taking pride in your work and not just doing it right the first time, but continually refactoring code to improve it over time.[^2] While Martin's core audience is probably software developers, scientists making scripts can also benefit from this advice. When you're in the code to fix a bug or add a feature, and the code is in your head, there is never a better time to clean it up and refactor. Building code improvement and maintenance into your work pays dividends over time, allowing you to realize the full benefits of coding. Below are some best practices to strive for that can help you develop "good code".

## A Disclaimer
The scientific coding universe is vast, and best practices are often application-specific. These "best practices" are especially focused on scientific Python. No workflow is perfect, and this isn’t an all-or-nothing proposition— any adoption of these practices will help!

## Tips for writing "Good Code"

* Break programs up into functions that ideally do one thing
* **DRY:** don't repeat yourself!
* Strive to generalize each function, but not at the cost of
simplicity
* Think about how you or someone else might want to use this in
the future, perhaps for a different application
* Think about **your collaborators** (which **include yourself 6 months from now!**)
* but **YAGNI:** you aren’t gonna need it
* Work in small steps and use version control[^3] (usually Git)
* Take the extra time to write detailed docstrings for each function, or at least enough for your collaborator(s) to understand why it's there and what it does.
* Plan for mistakes[^3]: add assertions and error traps to catch mistakes early
* Document your workflow so it can be re-run in the future. Even better; use a pipeline manager like [snakemake](https://snakemake.github.io/).
* Avoid writing object classes unless they are clearly needed
* Use a consistent organizational structure
* Put production code (that will be run repeatedly) in module files and scripts that can be run at the command line. Jupyter Notebooks are great for prototyping and illustration but can add to cognitive load in a production workflow.
* Remember the [Zen of Python](https://peps.python.org/pep-0020/#the-zen-of-python)
* Follow the community—when in doubt about how to do something, look at what others are doing online. What does Stack Overflow say? How are respected developers in mainstream Python packages approaching it?
* Don't be afraid to refactor!

### Variable names
should be expressive and searchable. 
  * For example, avoid single characters like `d` (what does "d" represent, and good luck trying to find it in a search)
  * Certainly avoid characters like `l` that can be confused with `1`, or `I`
  * Use nouns for objects and verbs for functions
  * Avoid "Hungarian" names like `PARCHGLIM` or `KVANI`[^2]
  * In Python, avoid built-ins like `file` (if you are using an editor with syntax highlighting, these should be obviously flagged in a different color)
  * In Python, follow [PEP8](https://peps.python.org/pep-0008/), which in most cases boils down to   lower case variable names with underscores if needed (CapWords for classes)
  * Some exceptions to these rules in Python:
      * Certainly universally followed conventions like `pd` for pandas
      * Perhaps also common but less universal idioms like using `k` and `v` for iterating through dictionaries. People do this because the context is usually clear (working with keys and values), and using `k` and `v` can reduce clutter and improve readability. Ditto for using `f` for file instead of the built-in `file` in for-loops or list comprehensions.
  * While you're in the code (and the code is in your head), take a little extra time to rename obtuse or unsearchable variables.

### On comments
In the book "Clean Code", Robert Martin argues forcefully that we should think critically about comments, and seek to minimize them. How many times have you copied and pasted, or refactored code, edited it until it works, and then moved on without touching the comments? We all do it, especially when we're pressed for time. It's quite easy to end up with a bunch of comments that are cryptic at best and at worse, misleading or irrelevant. These only serve to clutter up the code and increase the time needed understand it.
* If you're thinking about writing a comment, ask why? Can whatever the comment is be communicated directly in the code? For example:

    ```python
    # aggregate daily results to monthly means
    dfm = process_results(df)
    ```
    vs
    ```python
    monthly_means = get_monthly_means(daily_values)
    ```

    which one makes more sense to you?
* Use comments to document intent instead of repeating what the code is already saying. Sometimes, even with the most expressive code, the reason for a particular implementation choice isn't always clear, especially at a cursory glance. Well-placed comments can help with this.
* While you're in the code (and the code is in your head), take a little extra time to clean up stale or unnecessary comments.

### On AI assistants
* Use AI assistants as tools if they're helpful
* But recognize that there is no substitute for thinking
* [Stack Overflow](https://stackoverflow.com/questions), which has consensus-based answers from real software developers with years of experience, might yield better results.
* For example, a chatbot like *Claude* might spit out 100 lines of correctly formatted, [PEP8](https://peps.python.org/pep-0008/) compliant Python code that solves the problem, but the best solution might be 2 lines. Which code would you rather maintain?
* In other words, [There should be one-- and preferably only one --obvious way to do it.](https://peps.python.org/pep-0020/) The chatbot is unlikely to get this.
* This is a [problem that real software engineers are currently grappling with](https://leaddev.com/technical-direction/how-ai-generated-code-accelerates-technical-debt).


## Other Resources

* Does anyone have a favorite resource for learning Git?
* [Making a Python package](packaging)
* Are there any other resources that should be included here?


## References

[^1]: Abelson, H., Sussman, G. J., with Julie Sussman (1996). Structure and Interpretation of Computer Programs. Cambridge: MIT Press/McGraw-Hill, 855 p.

[^2]: Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship.

[^3]: Wilson G, Aruliah DA, Brown CT, Chue Hong NP, Davis M, et al. (2014) Best Practices for Scientific Computing. PLoS Biol 12(1): e1001745. [doi:10.1371/journal.pbio.1001745](https://doi.org/10.1371/journal.pbio.1001745)

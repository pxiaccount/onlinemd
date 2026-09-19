/**
 * Flashcards plugin (local) — renders Obsidian Spaced Repetition cards
 * (`คำถาม::คำตอบ` / `คำถาม::คำตอบ::คำใบ้`) after a heading containing
 * "flashcards" as collapsible HTML <details> cards.
 */
const FLASHCARD_CSS = `
.flashcard {
  border: 1px solid var(--lightgray);
  border-radius: 8px;
  margin: 0.5rem 0;
  background: var(--light);
}
.flashcard > summary {
  cursor: pointer;
  padding: 0.6rem 1rem;
  font-weight: 600;
  color: var(--dark);
}
.flashcard > summary:hover {
  background: var(--lightgray);
  border-radius: 8px;
}
.flashcard-answer {
  padding: 0.6rem 1rem;
  border-top: 1px dashed var(--lightgray);
  color: var(--darkgray);
}
.flashcard-hint {
  margin-top: 0.4rem;
  font-size: 0.9em;
  color: var(--gray);
}
`

export const Flashcards = () => {
  return {
    name: "Flashcards",
    textTransform(_ctx, src) {
      const lines = src.split(/\r?\n/)
      const out = []
      let inFlashcards = false
      for (const line of lines) {
        if (/^#{1,6}\s/.test(line)) {
          inFlashcards = /flashcards/i.test(line)
          out.push(line)
          continue
        }
        if (!inFlashcards) {
          out.push(line)
          continue
        }
        const m = line.match(/^(.+?)(?<!:)::(?!:)(.+?)(?:::(?!:)(.+))?$/)
        if (m && !line.trim().startsWith("[") && !line.includes("|")) {
          const q = m[1].trim()
          const a = m[2].trim()
          const hint = m[3] ? m[3].trim() : null
          out.push(
            `<details class="flashcard"><summary>${q}</summary><div class="flashcard-answer">${a}${hint ? `<div class="flashcard-hint">💡 ${hint}</div>` : ""}</div></details>`,
          )
        } else {
          out.push(line)
        }
      }
      return out.join("\n")
    },
    externalResources() {
      return {
        css: [{ content: FLASHCARD_CSS, inline: true }],
      }
    },
  }
}

export default Flashcards
export const manifest = {
  name: "flashcards",
  displayName: "Flashcards",
  description: "Obsidian Spaced Repetition flashcards as collapsible cards",
  version: "1.0.0",
  category: "transformer",
}

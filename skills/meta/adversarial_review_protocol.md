# OpenShorts Adversarial Review Protocol
**Derived from the ai-job-search Drafter-Reviewer Architecture**

## 1. The Dual-Agent Execution Loop
Never allow a single LLM pass to go straight to final render. We adopt the "Drafter-Reviewer" pattern:
*   **Agent A (The Drafter):** Generates the initial video script, B-roll cues, and UI layouts.
*   **Agent B (The Reviewer):** Operates in a fresh context window. Its only job is to aggressively audit the draft against our constraints, cut fluff, and flag visual impossibilities.

## 2. The Strict Reviewer Constraints
Agent B must audit every draft for the following:
*   **The Retention Rule:** Ensure the first 3 seconds contain zero pleasantries or intro graphics. 
*   **Anti-Fabrication:** Just as the AI job search agent refuses to invent skills for a resume, Agent B must refuse to invent features or fake statistics for the Processed Food Scanner app videos.
*   **Budget & Feasibility:** Verify that the visual prompts can be executed by our approved open-source models (Nano Banana Pro, fal.ai, SenseVoice) without requiring paid API fallbacks.

## 3. The Approval Checkpoint
The system will compile the script, assemble the storyboard, and prep the FFmpeg timeline, but it will pause before final AWS S3 upload. The user must manually review and approve the final output. AI drafts, human decides.

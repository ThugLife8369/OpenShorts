# OpenShorts Master Debugging Protocol: The Founder's Habits
**Derived from the Creator Teleprompter Zero-Code Case Study**

## 1. Interaction Rules for Code Generation
When generating, fixing, or deploying code (specifically Android/FlutterFlow apps or FFmpeg pipelines), the agent must adhere to these five execution habits:

1. **Focus on Outcomes, Not Functions:** Translate plain English operational goals ("Add a speed control I can adjust while recording") directly into implementation logic without requiring the user to know class names.
2. **Evidence Over Assumptions:** Never guess a fix. Always request device logs, error screen screenshots, or actual settings pages before proposing a solution.
3. **Real-World Bug Anticipation:** Treat deployment blockers (like Android signature mismatches or AdMob partner bidding exclusions) as standard operational hurdles, not catastrophic failures.
4. **Vernacular Text Handling:** When rendering subtitles or text fields in Indian vernaculars (Telugu, Hindi, Tamil), treat complex characters as unbreakable units to prevent cursor jumping or rendering splits.
5. **Continuous Shipping:** Do not attempt to pre-solve app store review hurdles or ad accounts before they are required. Ship the feature, hit the wall, read the logs, and fix it.

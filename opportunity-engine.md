# Opportunity Discovery Engine

**Created:** 2026-03-22
**For:** KORTA (Asistente Personal L7)
**Owner:** Lander

---

## 🔍 Purpose

Sistema automatizado para identificar oportunidades de alto ROI, gaps de automatización y tareas delegables.

---

## 📊 Opportunity Scoring

### Formula
```
Opportunity Score = (Impact × Confidence) / (Effort × Risk)

Impact: 1-10 (value generated)
Confidence: 0.1-1.0 (certainty of success)
Effort: 1-10 (hours required)
Risk: 1-5 (probability of failure)
```

### Thresholds
- **> 2.0:** Immediate action
- **1.0-2.0:** Queue for next sprint
- **< 1.0:** Archive, review quarterly

---

## 🔎 Discovery Categories

### 1. Unused Skills (Current: 40/52 missing)
**Scan Method:** `openclaw skills list`

| Skill | Category | Impact | Effort | Score |
|-------|----------|--------|--------|-------|
| apple-notes | Productivity | 7 | 2 | 3.5 |
| apple-reminders | Productivity | 8 | 2 | 4.0 |
| spotify-player | Entertainment | 5 | 1 | 5.0 |
| notion | Productivity | 9 | 3 | 3.0 |
| obsidian | Productivity | 8 | 2 | 4.0 |

**Action:** Install top 5 skills this week

---

### 2. Automation Gaps

**Current Manual Tasks (to automate):**
- [ ] Daily memory updates
- [ ] Git commit/push
- [ ] Heartbeat monitoring
- [ ] Skill discovery
- [ ] Task prioritization

**Automation Score:** 8/10 (high impact, low effort)

---

### 3. High-ROI Opportunities

| Opportunity | Impact | Effort | ROI | Priority |
|-------------|--------|--------|-----|----------|
| Calendar integration | 9 | 3 | 3.0 | P1 |
| Email automation | 8 | 4 | 2.0 | P1 |
| Note-taking workflow | 7 | 2 | 3.5 | P0 |
| Reminder system | 8 | 2 | 4.0 | P0 |
| File organization | 6 | 2 | 3.0 | P2 |

---

### 4. Delegable Tasks

**Current:** KORTA handles everything inline
**Target:** 70% delegation to sub-agents

**Tasks to Delegate:**
- Document creation → Codex/Claude
- Code review → Claude
- Research → Web search + summarize
- Data analysis → Pi
- Content generation → Any agent

---

## ✅ Opportunity Checklist

### Weekly Scan
- [ ] Run `openclaw skills list` → identify gaps
- [ ] Review active-tasks.md → find blockers
- [ ] Check mistakes-learned.md → prevent recurrence
- [ ] Analyze memory logs → spot patterns

### Monthly Review
- [ ] Calculate ROI of completed tasks
- [ ] Identify new automation candidates
- [ ] Update skill priorities
- [ ] Review delegation effectiveness

### Quarterly Strategy
- [ ] Reassess all opportunities
- [ ] Archive low-value items
- [ ] Set new targets
- [ ] Document learnings

---

## 🎯 Top 5 Immediate Actions

1. **Install apple-reminders skill** (Score: 4.0)
   - Impact: High - task management
   - Effort: Low - one command
   - Command: `npx clawhub install apple-reminders`

2. **Install spotify-player skill** (Score: 5.0)
   - Impact: Medium - entertainment control
   - Effort: Low - one command
   - Command: `npx clawhub install spotify-player`

3. **Setup auto-git commits** (Score: 3.5)
   - Impact: High - data safety
   - Effort: Low - cron job
   - Action: Create git auto-commit script

4. **Install notion skill** (Score: 3.0)
   - Impact: High - knowledge management
   - Effort: Medium - API setup
   - Command: `npx clawhub install notion`

5. **Create delegation templates** (Score: 4.0)
   - Impact: High - scalability
   - Effort: Medium - document patterns
   - Action: Create task templates

---

## 📈 Tracking Dashboard

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Skills Used | 12/52 | 40/52 | 🟡 |
| Tasks Delegated | 0% | 70% | 🔴 |
| Automation Rate | 10% | 80% | 🔴 |
| Avg Opportunity Score | - | >2.0 | - |

---

*Next Scan: 2026-03-29*
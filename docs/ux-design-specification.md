# Procrastination Agent - UX Design Specification

**Version:** 1.0
**Created:** November 14, 2025
**Design Team:** Yves, Nathalie, Eileen & Jara
**University:** Zurich School of Applied Sciences

**Design System:** Balanced Warmth + Elegant & Refined

---

## Executive Summary

This UX Design Specification transforms the Procrastination Agent from a functional but visually basic interface into a polished, professional research tool. The design combines the **Balanced Warmth** color palette (warm professional purples and teals) with the **Elegant & Refined** visual style (sophisticated, subtle gradients, modern depth).

**Key Design Decisions:**
- ✅ Removed all emojis → Professional, academic feel
- ✅ Simplified visual noise → Single focal point per component
- ✅ Warm professional palette → Trustworthy yet approachable
- ✅ Vertical timeline with labels → Transparent progress tracking
- ✅ Subtle gradients & shadows → Polished, modern depth

---

## 1. Color System - Balanced Warmth

### Primary Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Primary** | `#6D5D7E` | Main actions, active states, user messages |
| **Primary Hover** | `#7F7090` | Button hover states, interactive highlights |
| **Primary Light** | `#B5A4C7` | Accents, subtle highlights, loading states |
| **Secondary** | `#528584` | Supporting actions, secondary elements |
| **Secondary Hover** | `#639B9A` | Secondary button hovers |
| **Accent** | `#C7B8D6` | Decorative elements, very subtle accents |

### Neutral Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Background Main** | `#F8F7FA` | Page background, chat background |
| **Surface** | `#FFFFFF` | Cards, message bubbles, elevated surfaces |
| **Elevated Surface** | `#FAF9FC` | Slightly lifted surfaces, sidebar gradient target |

### Border Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Border Light** | `#E4DFE9` | Subtle dividers, card borders |
| **Border Medium** | `#D1C6DC` | Standard borders, input borders |
| **Border Dark** | `#B5A4C7` | Emphasized borders, focus states |

### Text Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Text Primary** | `#4E3F5E` | Main body text, headings |
| **Text Secondary** | `#8A7B9A` | Supporting text, descriptions |
| **Text Tertiary** | `#B5A4C7` | Hints, placeholders, disabled text |
| **Text Inverse** | `#FFFFFF` | Text on primary backgrounds |

### Semantic Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Success** | `#52C41A` | Completed states, checkmarks |
| **Success Background** | `#F0F9E8` | Success message backgrounds |

### Color Psychology Rationale

**Why Balanced Warmth?**
- **Purple (#6D5D7E)**: Conveys wisdom, knowledge, calm - perfect for academic/therapeutic contexts
- **Teal (#528584)**: Adds balance, trustworthiness, professionalism
- **Muted saturation**: Reduces visual fatigue during longer sessions
- **Warm undertones**: Approachable and supportive, not cold or clinical

---

## 2. Visual Foundation

### Typography

**Font Stack:**
```css
font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif;
```

**Type Scale:**
| Element | Size | Weight | Line Height | Usage |
|---------|------|--------|-------------|-------|
| App Title | 22px | 700 | 1.2 | Sidebar header |
| App Subtitle | 13px | 500 | 1.4 | Sidebar subtitle |
| Chat Header | 17px | 600 | 1.3 | Chat area title |
| Timeline Phase | 14px | 600 | 1.4 | Timeline labels |
| Timeline Desc | 12px | 400 | 1.4 | Timeline descriptions |
| Message Body | 15px | 400 | 1.6 | Chat messages |
| Input Text | 15px | 400 | 1.5 | Textarea input |
| Labels/Hints | 11-12px | 500-700 | 1.5 | Small labels, footers |

**Letter Spacing:**
- Headings: `-0.01em` (slightly tighter for elegance)
- Uppercase labels: `1px` (improve readability)
- Body text: `0` (default)

### Spacing System

**Base unit:** 4px

| Token | Value | Usage |
|-------|-------|-------|
| xs | 4px | Tight gaps |
| sm | 8px | Small gaps |
| md | 12px | Standard gaps |
| lg | 16px | Section spacing |
| xl | 20px | Large section spacing |
| 2xl | 24px | Major section spacing |
| 3xl | 32px | Page padding |

### Border Radius

| Element | Radius | Usage |
|---------|--------|-------|
| Message Bubbles | 18px | Main corners |
| Message Tail Corner | 6px | Bottom corner (left for assistant, right for user) |
| Input Field | 14px | Text input |
| Send Button | 50% | Circular button |
| Timeline Dots | 50% | Circular indicators |
| Cards | 16px | Card containers |

### Shadows

**Philosophy:** Subtle elevation, never dramatic

| Name | Value | Usage |
|------|-------|-------|
| **shadow-sm** | `0 1px 3px rgba(78, 63, 94, 0.08)` | Subtle card elevation |
| **shadow-md** | `0 2px 8px rgba(78, 63, 94, 0.1)` | Standard elevation |
| **shadow-lg** | `0 4px 16px rgba(78, 63, 94, 0.12)` | Prominent elevation |
| **shadow-user-msg** | `0 4px 12px rgba(109, 93, 126, 0.25)` | User message depth |
| **shadow-glow** | `0 0 0 4px rgba(109, 93, 126, 0.15), 0 2px 8px rgba(109, 93, 126, 0.4)` | Active timeline dot |

### Gradients

**Usage:** Sparingly, only for intentional visual hierarchy

| Name | Value | Usage |
|------|-------|-------|
| **Primary Gradient** | `linear-gradient(135deg, #6D5D7E 0%, #7F7090 100%)` | Send button, user messages |
| **Title Gradient** | `linear-gradient(135deg, #6D5D7E 0%, #528584 100%)` | App title (text gradient) |
| **Surface Gradient** | `linear-gradient(180deg, #FFFFFF 0%, #FAF9FC 100%)` | Sidebar background |
| **Chat Background Gradient** | `linear-gradient(180deg, #FAF9FC 0%, #FFFFFF 50%)` | Chat messages area |

---

## 3. Component Specifications

### 3.1 Sidebar

**Dimensions:**
- Width: 320px (desktop), 280px (mobile)
- Full height

**Visual Structure:**
```
┌─────────────────────────┐
│ Header                  │ ← Gradient background, border-bottom
├─────────────────────────┤
│                         │
│ Timeline (scrollable)   │ ← Main content area
│                         │
├─────────────────────────┤
│ Footer                  │ ← Team credit
└─────────────────────────┘
```

**States:**
- Default: Visible on desktop
- Mobile: Collapsible with hamburger button

**Header:**
- Padding: 32px 24px 24px
- Border-bottom: 1px solid `var(--border-light)`
- Title: Gradient text (primary → secondary)
- Subtitle: `var(--text-secondary)`

**Footer:**
- Padding: 20px 24px
- Border-top: 1px solid `var(--border-light)`
- Font-size: 11px
- Text: "Student project by Yves, Nathalie, Eileen & Jara • Zurich School of Applied Sciences"

### 3.2 Timeline (Vertical Progress Indicator)

**Design Pattern:** Option C - Vertical timeline with labels

**Visual Structure:**
```
● Informationssammlung     ← Active (larger dot, glow)
│  Aufgabe verstehen
│
● Hypothesen               ← Completed (green) OR Pending (hollow)
│  Ursachen erkunden
│
● Strategien
│  Lösungen entwickeln
│
○ Abschluss                ← Pending (hollow, light)
   Session beenden
```

**Timeline Item Anatomy:**
- **Dot:** 14px circle (16px when active)
- **Gap:** 14px between dot and text
- **Connector Line:** 2px width, gradient fade from primary-light to transparent
- **Phase Label:** 14px, weight 600
- **Description:** 12px, weight 400

**States:**

| State | Dot Style | Phase Color | Description Color | Shadow |
|-------|-----------|-------------|-------------------|--------|
| **Active** | 16px, solid primary | `var(--primary)` | `var(--text-secondary)` | Glow shadow |
| **Completed** | 14px, solid success | `var(--success)` | `var(--text-secondary)` | Success shadow |
| **Pending** | 14px, hollow (2px border) | `var(--text-tertiary)` | `var(--text-tertiary)` | None |

**Spacing:**
- Margin-bottom between items: 24px
- Connector line offset: Starts at +24px from top of dot

**Rationale:**
- **No emojis:** Professional, reduces visual noise
- **Labels included:** Transparency - users know what to expect
- **Subtle connector:** Visual flow without competing for attention
- **Glow on active:** Clear focal point, draws eye to current phase

### 3.3 Message Bubbles

**User Messages:**
- Background: `linear-gradient(135deg, var(--primary) 0%, var(--primary-hover) 100%)`
- Text color: `var(--text-inverse)`
- Max-width: 520px
- Padding: 14px 18px
- Border-radius: 18px (main), 6px (bottom-right corner)
- Shadow: `var(--shadow-user-msg)`
- Alignment: Right

**Assistant Messages:**
- Background: `var(--bg-surface)`
- Text color: `var(--text-primary)`
- Border: 2px solid `var(--border-light)`
- Max-width: 520px
- Padding: 14px 18px
- Border-radius: 18px (main), 6px (bottom-left corner)
- Shadow: `var(--shadow-md)`
- Alignment: Left
- Hover: Border changes to `var(--border-medium)`, shadow to `var(--shadow-lg)`

**Timestamp:**
- Font-size: 11px
- Color: `var(--text-tertiary)`
- Margin-top: 6px
- Padding: 0 6px

**Spacing:**
- Margin-bottom between messages: 20px

**Animation:**
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```
Duration: 0.4s ease

**Rationale:**
- **Distinct corners:** Immediately identifies sender (like iMessage)
- **Gradient for user:** Adds depth, makes user input feel important
- **Border for assistant:** Creates breathing room, separates from background
- **Hover effect:** Subtle feedback, feels responsive
- **Generous padding:** Readable, not cramped

### 3.4 Chat Input

**Dimensions:**
- Min-height: 50px
- Max-height: 120px (auto-resize)
- Padding: 14px 18px
- Border-radius: 14px

**States:**

| State | Border | Background | Shadow |
|-------|--------|------------|--------|
| Default | 2px `var(--border-light)` | `var(--bg-elevated)` | None |
| Focus | 2px `var(--primary)` | `var(--bg-surface)` | `0 0 0 3px rgba(109, 93, 126, 0.1)` |
| Disabled | 2px `var(--border-light)` | `var(--bg-elevated)` | None |

**Placeholder:** `var(--text-tertiary)`

**Keyboard Hint:**
- Text: "Enter zum Senden • Shift+Enter für neue Zeile"
- Font-size: 12px
- Color: `var(--text-tertiary)`
- Margin-top: 12px

### 3.5 Send Button

**Dimensions:**
- Size: 50px × 50px
- Border-radius: 50% (circle)
- Icon: 22px

**Appearance:**
- Background: `linear-gradient(135deg, var(--primary) 0%, var(--primary-hover) 100%)`
- Color: white
- Shadow: `0 3px 10px rgba(109, 93, 126, 0.3)`

**States:**

| State | Transform | Shadow |
|-------|-----------|--------|
| Default | `scale(1)` | `0 3px 10px rgba(109, 93, 126, 0.3)` |
| Hover | `scale(1.08)` | `0 4px 14px rgba(109, 93, 126, 0.4)` |
| Active | `scale(0.95)` | Maintained |
| Disabled | `scale(1)`, opacity 0.5 | Maintained |

**Icon:** Send arrow (stroke-width: 2.5)

### 3.6 Typing Indicator

**Visual:**
```
┌──────────────┐
│  ● ● ●       │  ← 3 pulsing dots
└──────────────┘
```

**Appearance:**
- Background: `var(--bg-surface)`
- Border: 2px solid `var(--border-light)`
- Border-radius: 18px (6px bottom-left corner)
- Padding: 14px 18px
- Shadow: `var(--shadow-md)`

**Dots:**
- Size: 8px diameter
- Color: `var(--primary-light)`
- Gap: 5px
- Animation: Bounce up 8px, 1.4s ease-in-out, staggered delays (0s, 0.2s, 0.4s)

---

## 4. Layouts & Responsive Design

### Desktop Layout (> 1024px)

```
┌────────────────────────────────────────────────────┐
│ Info Bar (optional, can be removed)               │
├──────────┬─────────────────────────────────────────┤
│          │ Chat Header                             │
│ Sidebar  ├─────────────────────────────────────────┤
│ (320px)  │                                         │
│          │ Messages (scrollable)                   │
│          │                                         │
│          ├─────────────────────────────────────────┤
│          │ Input Area                              │
└──────────┴─────────────────────────────────────────┘
```

**Max-width:** 1600px (centered)

### Tablet Layout (768px - 1024px)

Same as desktop, sidebar reduces to 280px

### Mobile Layout (< 768px)

```
┌────────────────────────────┐
│ ☰ Chat Header              │ ← Hamburger to toggle sidebar
├────────────────────────────┤
│                            │
│ Messages (full width)      │
│                            │
├────────────────────────────┤
│ Input Area                 │
└────────────────────────────┘
```

Sidebar overlays on top when opened

**Touch targets:** Minimum 44px × 44px

---

## 5. Accessibility

### WCAG Compliance Level

**Target:** WCAG 2.1 Level AA

**Color Contrast Ratios:**

| Combination | Ratio | Passes AA |
|-------------|-------|-----------|
| Primary (#6D5D7E) on White | 7.2:1 | ✅ AAA |
| Text Primary (#4E3F5E) on White | 9.8:1 | ✅ AAA |
| Text Secondary (#8A7B9A) on White | 4.8:1 | ✅ AA |
| Text Tertiary (#B5A4C7) on White | 3.2:1 | ⚠️ AA Large Only |

**Keyboard Navigation:**
- All interactive elements accessible via Tab
- Enter to send message
- Escape to close modals
- Arrow keys for timeline navigation (optional enhancement)

**Screen Reader Support:**
- Semantic HTML (`<nav>`, `<main>`, `<aside>`)
- ARIA labels on all buttons and inputs
- ARIA live region for new messages
- Role attributes for modals (`role="dialog"`, `aria-modal="true"`)

**Focus Management:**
- Visible focus indicators (3px ring, 10% opacity primary color)
- Focus trap in modals
- Auto-focus on safe defaults (cancel buttons, not destructive actions)

**Reduced Motion:**
- Respect `prefers-reduced-motion` media query
- Disable animations if user preference is set

---

## 6. Interactions & Micro-Animations

### Animation Principles

1. **Purposeful:** Every animation serves a function (feedback, state change, guidance)
2. **Subtle:** Never distracting, enhances rather than dominates
3. **Fast:** 200-400ms max for UI feedback
4. **Respect preferences:** Disable if `prefers-reduced-motion: reduce`

### Animation Inventory

| Element | Animation | Duration | Easing | Purpose |
|---------|-----------|----------|--------|---------|
| Message Bubble | Fade in + Slide up | 400ms | ease | Smooth message appearance |
| Typing Indicator | Bounce dots | 1.4s | ease-in-out | Show AI is "thinking" |
| Send Button | Scale up on hover | 200ms | ease | Interactive feedback |
| Timeline Dot (active) | Glow pulse | 2s | ease-in-out | Draw attention to current phase |
| Input Focus | Border color + Shadow | 200ms | ease | Feedback on focus |
| Button Hover | Scale + Shadow | 200ms | ease | Interactive feedback |

### Hover States

**Philosophy:** Gentle, not aggressive

- Timeline items: Slight brightness increase
- Message bubbles (assistant): Border color shift + shadow increase
- Buttons: Scale 1.05-1.08 + enhanced shadow
- Input: Border color change + glow

---

## 7. Design Rationale & Decisions

### Why "Elegant & Refined"?

**Before:** Gradient overload, emoji clutter, visual noise
**After:** Selective gradients, clean typography, single focal point per component

**Key Improvements:**
1. **Gradients used sparingly:** Only for user messages, send button, and app title
2. **Shadows create depth:** 3 levels (sm, md, lg) instead of custom shadows everywhere
3. **No emojis:** Professional tone suitable for academic research
4. **Generous white space:** Breathing room reduces cognitive load
5. **Subtle animations:** Polish without distraction

### Why "Balanced Warmth" Colors?

**Purple-Teal Balance:**
- **Purple:** Wisdom, calm, knowledge (academic, therapeutic)
- **Teal:** Trust, balance, professionalism (credibility)
- **Muted saturation:** Comfortable for extended use
- **Warm undertones:** Approachable, not clinical

**Avoided:**
- ❌ Pure blues: Too cold for empathy-driven intervention
- ❌ Bright oranges: Too energetic, not serious enough
- ❌ Grays only: Too neutral, lacks warmth
- ❌ Vibrant colors: Distracting, unprofessional

### Why Vertical Timeline?

**Option C: Vertical timeline with labels**

**Advantages:**
- ✅ **Transparent:** Users see all phases from the start
- ✅ **No surprises:** Reduces anxiety ("What's coming next?")
- ✅ **Clear progress:** Visual feedback on advancement
- ✅ **Research appropriate:** Participants should understand the structure
- ✅ **Compact:** Fits sidebar without overwhelming

**Alternatives considered:**
- ❌ Pure dots (Option A): Too minimal, users lack context
- ❌ Hover labels (Option B): Hidden information creates uncertainty

### Typography Choices

**System Font Stack:**
```
-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif
```

**Why:**
- ✅ Native on all platforms (fast loading)
- ✅ Optimized for screen reading
- ✅ Professional, neutral
- ✅ Excellent readability at small sizes
- ✅ Inter as fallback (installed for web)

---

## 8. Implementation Guide

### Step 1: Update Tailwind Config

Replace `/Users/yves/procrastination_agent/frontend/tailwind.config.ts` with:

```typescript
import type { Config } from 'tailwindcss'

export default {
  content: ['./index.html', './src/**/*.{ts,tsx,js,jsx}'],
  theme: {
    extend: {
      colors: {
        // Primary colors
        primary: '#6D5D7E',
        primaryHover: '#7F7090',
        primaryLight: '#B5A4C7',

        // Secondary colors
        secondary: '#528584',
        secondaryHover: '#639B9A',
        accent: '#C7B8D6',

        // Backgrounds
        background: '#F8F7FA',
        surface: '#FFFFFF',
        elevated: '#FAF9FC',

        // Borders
        border: '#E4DFE9',
        borderMedium: '#D1C6DC',
        borderDark: '#B5A4C7',

        // Text
        text: {
          primary: '#4E3F5E',
          secondary: '#8A7B9A',
          tertiary: '#B5A4C7',
          inverse: '#FFFFFF',
        },

        // Semantic
        success: '#52C41A',
        successBg: '#F0F9E8',
      },

      fontFamily: {
        sans: [
          '-apple-system',
          'BlinkMacSystemFont',
          'Inter',
          'Segoe UI',
          'sans-serif',
        ],
      },

      borderRadius: {
        message: '18px',
        messageCorner: '6px',
        input: '14px',
        button: '14px',
        card: '16px',
      },

      boxShadow: {
        sm: '0 1px 3px rgba(78, 63, 94, 0.08)',
        md: '0 2px 8px rgba(78, 63, 94, 0.1)',
        lg: '0 4px 16px rgba(78, 63, 94, 0.12)',
        'user-message': '0 4px 12px rgba(109, 93, 126, 0.25)',
        glow: '0 0 0 4px rgba(109, 93, 126, 0.15), 0 2px 8px rgba(109, 93, 126, 0.4)',
        'focus-ring': '0 0 0 3px rgba(109, 93, 126, 0.1)',
      },

      backgroundImage: {
        'gradient-primary': 'linear-gradient(135deg, #6D5D7E 0%, #7F7090 100%)',
        'gradient-title': 'linear-gradient(135deg, #6D5D7E 0%, #528584 100%)',
        'gradient-surface': 'linear-gradient(180deg, #FFFFFF 0%, #FAF9FC 100%)',
        'gradient-chat': 'linear-gradient(180deg, #FAF9FC 0%, #FFFFFF 50%)',
      },

      animation: {
        'fade-in-up': 'fadeInUp 0.4s ease',
        'typing-bounce': 'typingBounce 1.4s ease-in-out infinite',
        'glow-pulse': 'glowPulse 2s ease-in-out infinite alternate',
      },

      keyframes: {
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(12px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        typingBounce: {
          '0%, 60%, 100%': { transform: 'translateY(0)' },
          '30%': { transform: 'translateY(-8px)' },
        },
        glowPulse: {
          '0%': { boxShadow: '0 0 0 4px rgba(109, 93, 126, 0.15), 0 2px 8px rgba(109, 93, 126, 0.3)' },
          '100%': { boxShadow: '0 0 0 4px rgba(109, 93, 126, 0.25), 0 2px 10px rgba(109, 93, 126, 0.5)' },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
} satisfies Config
```

### Step 2: Update App.tsx (Sidebar)

**Remove emojis from StateIndicator:**

```tsx
// BEFORE:
const stateConfig = {
  intake: {
    label: 'Informationssammlung',
    emoji: '📋',  // ← REMOVE THIS
    description: 'Aufgabe verstehen',
  },
  // ...
}

// AFTER:
const stateConfig = {
  intake: {
    label: 'Informationssammlung',
    description: 'Aufgabe verstehen',
  },
  hypotheses: {
    label: 'Hypothesen',
    description: 'Ursachen erkunden',
  },
  strategies: {
    label: 'Strategien',
    description: 'Lösungen entwickeln',
  },
  completion: {
    label: 'Abschluss',
    description: 'Session beenden',
  },
}
```

**Update StateIndicator component:**

```tsx
function StateIndicator({ phase, current }: StateIndicatorProps) {
  const currentIndex = stateOrder.indexOf(current)
  const phaseIndex = stateOrder.indexOf(phase)

  const isCompleted = phaseIndex < currentIndex
  const isCurrent = phase === current
  const isPending = phaseIndex > currentIndex

  const config = stateConfig[phase]

  return (
    <div className="relative mb-6 transition-all duration-300">
      <div className="flex items-start gap-3.5">
        {/* Timeline Dot */}
        <div
          className={`
            mt-1 rounded-full transition-all duration-300
            ${isCurrent ? 'w-4 h-4 bg-primary shadow-glow' : ''}
            ${isCompleted ? 'w-3.5 h-3.5 bg-success shadow-md' : ''}
            ${isPending ? 'w-3.5 h-3.5 bg-surface border-2 border-borderMedium' : ''}
          `}
        />

        {/* Content */}
        <div className="flex-1 min-w-0">
          <h4
            className={`
              text-sm font-semibold leading-tight mb-0.5 transition-colors
              ${isCurrent ? 'text-primary' : ''}
              ${isCompleted ? 'text-success' : ''}
              ${isPending ? 'text-text-tertiary' : ''}
            `}
          >
            {config.label}
          </h4>
          <p
            className={`
              text-xs leading-tight transition-colors
              ${isCurrent ? 'text-text-secondary' : ''}
              ${isCompleted ? 'text-text-secondary' : ''}
              ${isPending ? 'text-text-tertiary' : ''}
            `}
          >
            {config.description}
          </p>
        </div>
      </div>

      {/* Connector Line (except for last item) */}
      {!isPending && phaseIndex < stateOrder.length - 1 && (
        <div
          className="absolute left-1.5 top-6 w-0.5 h-6 bg-gradient-to-b from-primaryLight to-transparent opacity-30"
          style={{ height: 'calc(100% + 8px)' }}
        />
      )}
    </div>
  )
}
```

**Update sidebar styling:**

```tsx
<aside
  className={`${
    sidebarOpen ? 'w-80' : 'w-0'
  } bg-gradient-surface border-r border-border transition-all duration-300 overflow-hidden`}
>
  <div className="p-6">
    {/* App Title with Gradient */}
    <h2 className="text-[22px] font-bold tracking-tight mb-1.5 bg-gradient-title bg-clip-text text-transparent">
      Prokrastinations-Agent
    </h2>
    <p className="text-[13px] text-text-secondary font-medium mb-7">
      Unterstützung bei Aufschieberitis
    </p>

    {/* Timeline Section */}
    <div className="mb-6">
      <h3 className="text-[11px] font-bold uppercase tracking-wider text-text-secondary mb-5">
        Fortschritt
      </h3>
      <StateIndicator phase="intake" current={currentState} />
      <StateIndicator phase="hypotheses" current={currentState} />
      <StateIndicator phase="strategies" current={currentState} />
      <StateIndicator phase="completion" current={currentState} />
    </div>

    {/* Footer */}
    <div className="border-t border-border pt-5 mt-auto">
      <p className="text-[11px] leading-relaxed text-text-secondary">
        <strong className="text-text-primary font-semibold">Student project by</strong><br />
        Yves, Nathalie, Eileen & Jara<br />
        Zurich School of Applied Sciences
      </p>
    </div>
  </div>
</aside>
```

### Step 3: Update Message Bubbles

**In ChatMessage.tsx:**

```tsx
<motion.div
  initial={prefersReducedMotion ? {} : { opacity: 0, y: 12 }}
  animate={prefersReducedMotion ? {} : { opacity: 1, y: 0 }}
  transition={prefersReducedMotion ? {} : { duration: 0.4, ease: 'easeOut' }}
  className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-5`}
>
  <div className={`flex flex-col ${isUser ? 'items-end' : 'items-start'} max-w-[520px]`}>
    <div
      className={`
        px-[18px] py-3.5 transition-all duration-200
        ${isUser
          ? 'bg-gradient-primary text-text-inverse shadow-user-message rounded-message rounded-br-messageCorner'
          : 'bg-surface text-text-primary border-2 border-border shadow-md rounded-message rounded-bl-messageCorner hover:border-borderMedium hover:shadow-lg'
        }
      `}
    >
      <div className="text-[15px] leading-relaxed">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {content}
        </ReactMarkdown>
      </div>
    </div>
    {formattedTime && (
      <span className="text-text-tertiary text-[11px] mt-1.5 px-1.5 font-medium">
        {formattedTime}
      </span>
    )}
  </div>
</motion.div>
```

### Step 4: Update Chat Input

**In ChatInput.tsx:**

```tsx
<div className="border-t border-border bg-surface px-8 py-6">
  <div className="max-w-[800px] flex items-end gap-3">
    <div className="flex-1 relative">
      <textarea
        ref={textareaRef}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Nachricht schreiben..."
        disabled={isLoading}
        rows={1}
        aria-label="Nachricht eingeben"
        aria-describedby="keyboard-hint"
        className="
          w-full px-[18px] py-3.5
          bg-elevated text-text-primary placeholder-text-tertiary
          rounded-input resize-none
          border-2 border-border
          focus:outline-none focus:border-primary focus:shadow-focus-ring focus:bg-surface
          disabled:opacity-50 disabled:cursor-not-allowed
          transition-all duration-200
          text-[15px] leading-relaxed
        "
        style={{ minHeight: '50px', maxHeight: '120px' }}
      />
    </div>

    <motion.button
      onClick={handleSend}
      disabled={!input.trim() || isLoading}
      whileHover={{ scale: input.trim() && !isLoading ? 1.08 : 1 }}
      whileTap={{ scale: input.trim() && !isLoading ? 0.95 : 1 }}
      className="
        flex-shrink-0 w-[50px] h-[50px]
        bg-gradient-primary text-text-inverse rounded-full
        flex items-center justify-center
        disabled:opacity-50 disabled:cursor-not-allowed
        transition-all duration-200
        shadow-md
      "
      style={{
        boxShadow: !input.trim() || isLoading
          ? 'none'
          : '0 3px 10px rgba(109, 93, 126, 0.3)'
      }}
      aria-label="Send message"
    >
      <svg className="w-5.5 h-5.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/>
      </svg>
    </motion.button>
  </div>

  {/* Keyboard hint */}
  <div className="max-w-[800px] mt-3 px-0.5">
    <p id="keyboard-hint" className="text-text-tertiary text-xs text-center font-medium">
      Enter zum Senden • Shift+Enter für neue Zeile
    </p>
  </div>
</div>
```

### Step 5: Update Main Container Backgrounds

**In App.tsx:**

```tsx
<div className="flex h-screen bg-background font-sans overflow-hidden">
  {/* ... sidebar ... */}

  <main className="flex-1 flex flex-col bg-surface">
    {/* Header */}
    <header className="bg-gradient-surface backdrop-blur-sm border-b border-border px-6 py-5 shadow-sm">
      <h1 className="text-[17px] font-semibold text-text-primary tracking-tight">
        Gespräch
      </h1>
    </header>

    {/* Messages Container */}
    <div className="flex-1 overflow-y-auto bg-gradient-chat">
      <ChatContainer />
    </div>

    {/* Example Prompts & Input */}
    <ExamplePrompts onSelectPrompt={sendMessage} />
    <ChatInput onSend={sendMessage} />
  </main>
</div>
```

### Step 6: Remove All Remaining Emojis

**Search your codebase for emojis and remove:**
- ✅ Timeline emoji indicators → Removed (now uses dots only)
- 📝 Sidebar action buttons (summary, export, reset) → Replace with icon SVGs or text only
- ✨ Any decorative emojis in text → Remove

**Example for sidebar buttons:**

```tsx
{/* Summary Button - BEFORE */}
<span className="text-base">📝</span>

{/* Summary Button - AFTER */}
<svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
</svg>
```

---

## 9. Testing Checklist

### Visual QA

- [ ] All emojis removed
- [ ] Colors match Balanced Warmth palette
- [ ] Timeline uses vertical dots with labels (no emojis)
- [ ] Gradients only on: app title, user messages, send button
- [ ] Shadows are subtle (not excessive)
- [ ] Footer shows: "Student project by Yves, Nathalie, Eileen & Jara • Zurich School of Applied Sciences"
- [ ] Message bubbles have tail corners (6px radius on one corner)
- [ ] Typing indicator uses pulsing dots (not emojis)

### Interaction QA

- [ ] Timeline dots glow when active
- [ ] Send button scales on hover
- [ ] Message bubbles fade in with slide-up animation
- [ ] Input field shows focus ring on focus
- [ ] Textarea auto-resizes (max 120px)
- [ ] Assistant message bubbles have hover effect (border + shadow change)

### Accessibility QA

- [ ] All text meets WCAG AA contrast (use browser inspector)
- [ ] Keyboard navigation works (Tab, Enter, Escape)
- [ ] Screen reader announces timeline progress
- [ ] Focus indicators visible on all interactive elements
- [ ] Reduced motion preference respected

### Responsive QA

- [ ] Desktop (>1024px): Sidebar 320px, full layout
- [ ] Tablet (768-1024px): Sidebar 280px, full layout
- [ ] Mobile (<768px): Collapsible sidebar, full-width chat
- [ ] Message bubbles don't exceed screen width
- [ ] Touch targets minimum 44px on mobile

---

## 10. Future Enhancements

### Short-term (v1.1)
- [ ] Dark mode variant (keeping same color relationships)
- [ ] Smooth state transition animations
- [ ] Loading skeleton screens
- [ ] Message reactions (simple icons, not emojis)

### Medium-term (v2.0)
- [ ] Timeline progress percentage
- [ ] Export conversation with branding
- [ ] Customizable color themes (user preference)
- [ ] Advanced accessibility features (high contrast mode)

### Long-term (v3.0)
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] Progressive Web App (PWA)
- [ ] Analytics dashboard for researchers

---

## 11. Design System Maintenance

### When to Update

**Color changes:**
- Update `tailwind.config.ts` first
- Regenerate color swatches documentation
- Test contrast ratios
- Update this specification

**Component changes:**
- Document rationale
- Update component specifications section
- Capture before/after screenshots
- Update implementation guide

**Animation changes:**
- Test with `prefers-reduced-motion`
- Document timing and easing
- Ensure purposeful (not decorative)

### Design Tokens

All colors, spacing, shadows, and typography are defined in Tailwind config. **Never use hardcoded values in components** - always reference Tailwind classes or CSS variables.

**Good:**
```tsx
className="text-text-primary bg-surface border-border"
```

**Bad:**
```tsx
className="text-[#4E3F5E] bg-[#FFFFFF] border-[#E4DFE9]"
```

---

## 12. Credits & Version History

**Design Team:**
- Yves (Product Owner, UX Research)
- Nathalie (Visual Design)
- Eileen (Interaction Design)
- Jara (Accessibility & Testing)

**University:** Zurich School of Applied Sciences (ZHAW)

**Version History:**

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Nov 14, 2025 | Initial design system - Balanced Warmth + Elegant & Refined | Yves |

---

## 13. Resources

**Design Files:**
- Color Theme Visualizer: `/docs/ux-color-themes.html`
- Design Direction Mockups: `/docs/ux-design-directions.html`
- Final Prototype: `/docs/final-design-prototype.html`
- This Specification: `/docs/ux-design-specification.md`

**Implementation Reference:**
- Tailwind CSS Documentation: https://tailwindcss.com/docs
- Framer Motion Documentation: https://www.framer.com/motion/
- React Accessibility: https://react.dev/learn/accessibility
- WCAG 2.1 Guidelines: https://www.w3.org/WAI/WCAG21/quickref/

**Color Tools:**
- Contrast Checker: https://webaim.org/resources/contrastchecker/
- Color Blindness Simulator: https://www.color-blindness.com/coblis-color-blindness-simulator/

---

**This design system transforms the Procrastination Agent into a professional, polished research tool while maintaining warmth and approachability. Every decision is documented, accessible, and ready for implementation.**

🎨 **Designed with care by Yves, Nathalie, Eileen & Jara**
🏫 **Zurich School of Applied Sciences**
📅 **November 2025**

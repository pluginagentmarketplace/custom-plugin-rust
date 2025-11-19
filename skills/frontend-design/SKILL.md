---
name: frontend-ui-design-systems
description: Master modern frontend development, UI/UX design principles, responsive design, component architecture, and design systems. Includes HTML, CSS, JavaScript, TypeScript, React, Next.js, Vue, Angular, React Native, and UX/Design system fundamentals.
---

# Frontend & UI/Design Systems

## Quick Start

Modern frontend development requires understanding multiple layers:

### HTML Foundation
```html
<header role="banner" aria-label="Site header">
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
    </ul>
  </nav>
</header>
<main role="main">
  <article>Content</article>
</main>
```

### CSS Modern Techniques
```css
/* CSS Grid for layouts */
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

/* Flexbox for components */
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* CSS Variables for theming */
:root {
  --primary: #3b82f6;
  --spacing: 1rem;
}
```

### JavaScript Modern Patterns
```javascript
// Async/await pattern
async function fetchUserData(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    return await response.json();
  } catch (error) {
    console.error('Error:', error);
  }
}

// Array methods
const users = data
  .filter(user => user.active)
  .map(user => ({ id: user.id, name: user.name }))
  .sort((a, b) => a.name.localeCompare(b.name));
```

### React Component Patterns
```javascript
// Function component with hooks
import { useState, useEffect, useCallback } from 'react';

export function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUser(userId).then(setUser).finally(() => setLoading(false));
  }, [userId]);

  const handleUpdate = useCallback((data) => {
    // Memoized update handler
  }, []);

  if (loading) return <div>Loading...</div>;
  return (
    <div role="region" aria-live="polite">
      {user && <h1>{user.name}</h1>}
    </div>
  );
}
```

### TypeScript for Type Safety
```typescript
interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

interface ApiResponse<T> {
  data: T;
  status: number;
  error?: string;
}

async function getUser(id: string): Promise<ApiResponse<User>> {
  // Type-safe implementation
}
```

### Next.js Full-Stack
```javascript
// pages/api/users/[id].js - API Route
export default async function handler(req, res) {
  if (req.method === 'GET') {
    const user = await db.users.findById(req.query.id);
    res.status(200).json(user);
  }
}

// pages/users/[id].js - Page with SSR
export async function getServerSideProps({ params }) {
  const user = await fetchUser(params.id);
  return { props: { user } };
}
```

### Design System Component
```javascript
// Button component that follows design system
export const Button = ({
  variant = 'primary',
  size = 'md',
  children,
  ...props
}) => (
  <button
    className={`btn btn-${variant} btn-${size}`}
    {...props}
  >
    {children}
  </button>
);

// Design tokens in CSS
const tokens = {
  colors: {
    primary: '#3b82f6',
    secondary: '#10b981',
  },
  spacing: {
    xs: '0.25rem',
    sm: '0.5rem',
    md: '1rem',
    lg: '1.5rem',
  },
};
```

## Learning Paths

### Frontend Beginner → Advanced
1. **HTML Fundamentals** (roadmap.sh/html)
   - Semantic markup
   - Accessibility (WCAG)
   - Forms and validation

2. **CSS Mastery** (roadmap.sh/css)
   - Responsive design
   - Flexbox & Grid
   - CSS animations
   - CSS-in-JS solutions

3. **JavaScript Deep Dive** (roadmap.sh/javascript)
   - ES6+ features
   - DOM manipulation
   - Async patterns
   - Event handling

4. **TypeScript** (roadmap.sh/typescript)
   - Type annotations
   - Interfaces & types
   - Generics
   - Module system

5. **React** (roadmap.sh/react)
   - Hooks (useState, useEffect, useContext)
   - State management
   - Component composition
   - Performance optimization

6. **Next.js** (roadmap.sh/nextjs)
   - File-based routing
   - Server-side rendering
   - API routes
   - Image optimization

### Framework Alternatives
- **Vue.js** (roadmap.sh/vue) - Progressive framework with composition API
- **Angular** (roadmap.sh/angular) - Full-featured enterprise framework
- **React Native** (roadmap.sh/react-native) - Cross-platform mobile

### Design & UX
- **UX Design** (roadmap.sh/ux-design)
  - User research
  - Wireframing
  - Prototyping
  - Usability testing

- **Design Systems** (roadmap.sh/design-system)
  - Component libraries
  - Design tokens
  - Documentation
  - Versioning

## Performance Optimization

```javascript
// Code splitting
import dynamic from 'next/dynamic';

const HeavyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <div>Loading...</div>,
});

// Image optimization
import Image from 'next/image';

<Image
  src="/image.png"
  alt="Description"
  width={400}
  height={300}
  loading="lazy"
/>

// Memoization
const Component = memo(({ data }) => {
  return <div>{data.name}</div>;
}, (prev, next) => prev.data.id === next.data.id);
```

## Testing Frontend

```javascript
// Component testing with React Testing Library
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('button click handler', async () => {
  const handleClick = jest.fn();
  render(<Button onClick={handleClick}>Click me</Button>);

  await userEvent.click(screen.getByRole('button'));
  expect(handleClick).toHaveBeenCalled();
});
```

## Key Frameworks & Libraries

| Framework | Use Case | Learning Time |
|-----------|----------|------------------|
| React | Component-based, large ecosystems | 2-3 weeks |
| Next.js | Full-stack, SSR/SSG | 3-4 weeks |
| Vue | Progressive, gentle learning curve | 1-2 weeks |
| Angular | Enterprise, full-featured | 4-6 weeks |
| React Native | Mobile apps with React | 2-3 weeks |

## Accessibility (A11y) Checklist

- [ ] Semantic HTML (header, nav, main, article)
- [ ] ARIA labels and roles
- [ ] Keyboard navigation
- [ ] Color contrast (WCAG AA minimum)
- [ ] Alt text for images
- [ ] Focus visible indicators
- [ ] Screen reader testing
- [ ] Mobile responsiveness

## Resources

- [MDN Web Docs](https://developer.mozilla.org)
- [Web.dev](https://web.dev)
- [Can I Use](https://caniuse.com) - Browser compatibility
- [WebAIM](https://webaim.org) - Accessibility resources

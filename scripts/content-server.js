#!/usr/bin/env node

/**
 * Learning Content Server
 * Serves roadmap data and learning content for the custom-plugin-rust
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

// Roadmap data with 71+ roles
const ROADMAP_DATA = {
  frontendRoles: [
    'html', 'css', 'javascript', 'typescript', 'react', 'nextjs',
    'vue', 'angular', 'react-native', 'ux-design', 'design-systems'
  ],
  backendRoles: [
    'nodejs', 'graphql', 'spring-boot', 'aspnet-core', 'php',
    'api-design', 'backend', 'backend-beginner'
  ],
  languageRoles: [
    'python', 'java', 'go', 'rust', 'cpp', 'kotlin', 'bash',
    'computer-science', 'data-structures-algorithms'
  ],
  dataAiRoles: [
    'ai-engineer', 'ai-data-scientist', 'machine-learning', 'mlops',
    'prompt-engineering', 'ai-red-teaming', 'ai-agents',
    'data-analyst', 'bi-analyst', 'data-engineer'
  ],
  cloudDevopsRoles: [
    'aws', 'cloudflare', 'docker', 'kubernetes', 'terraform',
    'linux', 'devops', 'devops-beginner', 'system-design'
  ],
  databaseRoles: [
    'postgresql-dba', 'sql', 'redis', 'mongodb',
    'software-design-architecture', 'software-architect'
  ],
  mobileSpecializedRoles: [
    'ios', 'swift-ui', 'android', 'flutter', 'git-github',
    'full-stack', 'blockchain', 'game-developer',
    'server-side-game-developer', 'qa', 'product-manager',
    'engineering-manager', 'technical-writer', 'devrel', 'cyber-security'
  ]
};

const server = http.createServer((req, res) => {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Content-Type', 'application/json');

  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }

  const { pathname, searchParams } = new URL(req.url, `http://${req.headers.host}`);

  // Routes
  if (pathname === '/api/roadmaps') {
    // Get all roadmaps
    res.writeHead(200);
    res.end(JSON.stringify({
      success: true,
      totalRoles: 71,
      data: ROADMAP_DATA
    }));
  } else if (pathname === '/api/roadmap') {
    // Get specific roadmap
    const role = searchParams.get('role');
    if (!role) {
      res.writeHead(400);
      res.end(JSON.stringify({ error: 'Role parameter required' }));
      return;
    }

    res.writeHead(200);
    res.end(JSON.stringify({
      success: true,
      role: role,
      data: generateRoadmapForRole(role)
    }));
  } else if (pathname === '/api/learning-path') {
    // Get personalized learning path
    const role = searchParams.get('role');
    const level = searchParams.get('level') || 'beginner';

    res.writeHead(200);
    res.end(JSON.stringify({
      success: true,
      role: role,
      level: level,
      path: generateLearningPath(role, level)
    }));
  } else if (pathname === '/api/agents') {
    // Get all agents
    res.writeHead(200);
    res.end(JSON.stringify({
      success: true,
      agents: [
        { id: 1, name: 'Frontend & UI/Design Specialist' },
        { id: 2, name: 'Backend & API Development Specialist' },
        { id: 3, name: 'Languages & Core Programming Specialist' },
        { id: 4, name: 'Data, AI & Machine Learning Specialist' },
        { id: 5, name: 'Cloud, DevOps & Infrastructure Specialist' },
        { id: 6, name: 'Databases & Architecture Specialist' },
        { id: 7, name: 'Mobile, Blockchain & Specialized Roles Specialist' }
      ]
    }));
  } else {
    res.writeHead(404);
    res.end(JSON.stringify({ error: 'Route not found' }));
  }
});

function generateRoadmapForRole(role) {
  return {
    title: `${role.charAt(0).toUpperCase() + role.slice(1)} Roadmap`,
    duration: '4-12 weeks',
    difficulty: 'intermediate',
    phases: [
      {
        phase: 1,
        name: 'Fundamentals',
        duration: '1-2 weeks',
        topics: ['Core concepts', 'Basic tools', 'Environment setup']
      },
      {
        phase: 2,
        name: 'Core Skills',
        duration: '2-4 weeks',
        topics: ['Intermediate concepts', 'Practical projects', 'Best practices']
      },
      {
        phase: 3,
        name: 'Advanced Topics',
        duration: '2-4 weeks',
        topics: ['Advanced patterns', 'Performance optimization', 'Production deployment']
      },
      {
        phase: 4,
        name: 'Specialization',
        duration: '2-4 weeks',
        topics: ['Advanced specialization', 'Real-world projects', 'Career development']
      }
    ],
    resources: [
      'Official documentation',
      'Recommended courses',
      'Practice projects',
      'Community forums'
    ]
  };
}

function generateLearningPath(role, level) {
  const weeklySchedule = {
    beginner: {
      hoursPerWeek: 20,
      totalWeeks: 12,
      focusAreas: ['Fundamentals', 'Core Concepts', 'Basic Projects']
    },
    intermediate: {
      hoursPerWeek: 15,
      totalWeeks: 8,
      focusAreas: ['Advanced Concepts', 'Complex Projects', 'Best Practices']
    },
    advanced: {
      hoursPerWeek: 10,
      totalWeeks: 6,
      focusAreas: ['Specialization', 'Performance Tuning', 'Architecture']
    }
  };

  return weeklySchedule[level] || weeklySchedule.beginner;
}

const PORT = process.env.PORT || 3333;
server.listen(PORT, () => {
  console.log(`Learning Content Server running on port ${PORT}`);
  console.log(`Available endpoints:`);
  console.log(`  GET /api/roadmaps - Get all roadmaps`);
  console.log(`  GET /api/roadmap?role=<role> - Get specific roadmap`);
  console.log(`  GET /api/learning-path?role=<role>&level=<level> - Get learning path`);
  console.log(`  GET /api/agents - Get all agents`);
});

module.exports = server;

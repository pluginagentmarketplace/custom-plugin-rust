#!/usr/bin/env node

/**
 * Skill Matcher
 * Matches user skills with recommended learning paths and resources
 */

class SkillMatcher {
  constructor() {
    this.skillMap = this.initializeSkillMap();
    this.learningPaths = this.initializeLearningPaths();
  }

  /**
   * Initialize skill to agent mapping
   */
  initializeSkillMap() {
    return {
      // Frontend skills
      'html': { agent: 1, category: 'Frontend' },
      'css': { agent: 1, category: 'Frontend' },
      'javascript': { agent: 1, category: 'Frontend' },
      'typescript': { agent: 1, category: 'Frontend' },
      'react': { agent: 1, category: 'Frontend' },
      'nextjs': { agent: 1, category: 'Frontend' },
      'vue': { agent: 1, category: 'Frontend' },
      'angular': { agent: 1, category: 'Frontend' },
      'ux-design': { agent: 1, category: 'Frontend' },

      // Backend skills
      'nodejs': { agent: 2, category: 'Backend' },
      'graphql': { agent: 2, category: 'Backend' },
      'spring-boot': { agent: 2, category: 'Backend' },
      'aspnet-core': { agent: 2, category: 'Backend' },
      'php': { agent: 2, category: 'Backend' },
      'api-design': { agent: 2, category: 'Backend' },

      // Language skills
      'python': { agent: 3, category: 'Languages' },
      'java': { agent: 3, category: 'Languages' },
      'go': { agent: 3, category: 'Languages' },
      'rust': { agent: 3, category: 'Languages' },
      'cpp': { agent: 3, category: 'Languages' },
      'kotlin': { agent: 3, category: 'Languages' },

      // Data/AI skills
      'machine-learning': { agent: 4, category: 'Data/AI' },
      'deep-learning': { agent: 4, category: 'Data/AI' },
      'mlops': { agent: 4, category: 'Data/AI' },
      'data-science': { agent: 4, category: 'Data/AI' },
      'prompt-engineering': { agent: 4, category: 'Data/AI' },

      // Cloud/DevOps skills
      'aws': { agent: 5, category: 'Cloud' },
      'docker': { agent: 5, category: 'Cloud' },
      'kubernetes': { agent: 5, category: 'Cloud' },
      'terraform': { agent: 5, category: 'Cloud' },
      'system-design': { agent: 5, category: 'Cloud' },

      // Database skills
      'postgresql': { agent: 6, category: 'Databases' },
      'sql': { agent: 6, category: 'Databases' },
      'mongodb': { agent: 6, category: 'Databases' },
      'redis': { agent: 6, category: 'Databases' },

      // Mobile/Specialized skills
      'ios': { agent: 7, category: 'Mobile' },
      'android': { agent: 7, category: 'Mobile' },
      'flutter': { agent: 7, category: 'Mobile' },
      'blockchain': { agent: 7, category: 'Specialized' },
      'game-dev': { agent: 7, category: 'Specialized' }
    };
  }

  /**
   * Initialize learning paths
   */
  initializeLearningPaths() {
    return {
      'frontend-specialist': {
        skills: ['html', 'css', 'javascript', 'typescript', 'react'],
        agent: 1,
        duration: '8-10 weeks',
        level: 'intermediate'
      },
      'backend-specialist': {
        skills: ['api-design', 'nodejs', 'databases', 'system-design'],
        agent: 2,
        duration: '10-12 weeks',
        level: 'intermediate'
      },
      'full-stack': {
        skills: ['javascript', 'react', 'nodejs', 'databases'],
        agent: [1, 2],
        duration: '12-16 weeks',
        level: 'advanced'
      },
      'devops-engineer': {
        skills: ['docker', 'kubernetes', 'aws', 'system-design'],
        agent: 5,
        duration: '10-12 weeks',
        level: 'intermediate'
      },
      'ml-engineer': {
        skills: ['python', 'machine-learning', 'data-science', 'mlops'],
        agent: [3, 4],
        duration: '12-16 weeks',
        level: 'advanced'
      }
    };
  }

  /**
   * Match user to agent
   */
  matchUserToAgent(requestedSkills) {
    const agentScores = new Map();

    requestedSkills.forEach(skill => {
      const skillInfo = this.skillMap[skill.toLowerCase()];
      if (skillInfo) {
        const agent = skillInfo.agent;
        agentScores.set(agent, (agentScores.get(agent) || 0) + 1);
      }
    });

    if (agentScores.size === 0) {
      return null;
    }

    const bestAgent = Array.from(agentScores.entries())
      .reduce((prev, current) => (prev[1] > current[1]) ? prev : current)[0];

    return bestAgent;
  }

  /**
   * Recommend learning path
   */
  recommendLearningPath(userGoal, currentSkills = []) {
    const pathInfo = this.learningPaths[userGoal];
    if (!pathInfo) {
      return null;
    }

    // Calculate skill gaps
    const skillGaps = pathInfo.skills.filter(skill => !currentSkills.includes(skill));
    const progressPercent = Math.round((
      (pathInfo.skills.length - skillGaps.length) / pathInfo.skills.length
    ) * 100);

    return {
      goal: userGoal,
      agent: pathInfo.agent,
      duration: pathInfo.duration,
      level: pathInfo.level,
      requiredSkills: pathInfo.skills,
      skillGaps: skillGaps,
      completionPercent: progressPercent,
      nextSteps: this.generateNextSteps(skillGaps),
      resources: this.getResourcesForPath(userGoal)
    };
  }

  /**
   * Generate next steps
   */
  generateNextSteps(skillGaps) {
    return skillGaps.map((skill, index) => ({
      step: index + 1,
      skill: skill,
      estimatedTime: '5-7 days',
      activities: [
        `Learn ${skill} fundamentals`,
        `Complete practice exercises`,
        `Build mini project`,
        `Take assessment`
      ]
    }));
  }

  /**
   * Get resources for learning path
   */
  getResourcesForPath(path) {
    const resources = {
      'frontend-specialist': [
        { title: 'MDN Web Docs', url: 'https://developer.mozilla.org' },
        { title: 'React Official Docs', url: 'https://react.dev' },
        { title: 'Web.dev', url: 'https://web.dev' }
      ],
      'backend-specialist': [
        { title: 'Node.js Docs', url: 'https://nodejs.org/docs' },
        { title: 'RESTful API Docs', url: 'https://restfulapi.net' },
        { title: 'System Design Primer', url: 'https://github.com/donnemartin/system-design-primer' }
      ],
      'devops-engineer': [
        { title: 'Kubernetes Docs', url: 'https://kubernetes.io/docs' },
        { title: 'Docker Documentation', url: 'https://docs.docker.com' },
        { title: 'AWS Documentation', url: 'https://docs.aws.amazon.com' }
      ],
      'ml-engineer': [
        { title: 'PyTorch Docs', url: 'https://pytorch.org/docs' },
        { title: 'TensorFlow Guide', url: 'https://www.tensorflow.org/guide' },
        { title: 'Fast.ai', url: 'https://fast.ai' }
      ]
    };

    return resources[path] || [];
  }

  /**
   * Suggest career paths
   */
  suggestCareerPaths(userSkills, experience = 'junior') {
    const suggestions = [];

    // Analyze skills
    const agentMatch = this.matchUserToAgent(userSkills);

    // Generate suggestions based on agent and experience
    if (agentMatch === 1) { // Frontend
      suggestions.push({
        path: 'frontend-specialist',
        difficulty: 'intermediate',
        timeToNext: '3-4 months'
      });
      suggestions.push({
        path: 'full-stack',
        difficulty: 'advanced',
        timeToNext: '6-8 months'
      });
    } else if (agentMatch === 5) { // Cloud/DevOps
      suggestions.push({
        path: 'devops-engineer',
        difficulty: 'intermediate',
        timeToNext: '4-5 months'
      });
    }

    return suggestions;
  }
}

module.exports = SkillMatcher;

if (require.main === module) {
  const matcher = new SkillMatcher();

  // Example: Match user to agent
  const userSkills = ['javascript', 'react', 'typescript'];
  const agent = matcher.matchUserToAgent(userSkills);
  console.log('Best matching agent:', agent);

  // Example: Recommend learning path
  const recommendation = matcher.recommendLearningPath('full-stack', userSkills);
  console.log('\nLearning Path Recommendation:');
  console.log(JSON.stringify(recommendation, null, 2));

  // Example: Career suggestions
  const careers = matcher.suggestCareerPaths(userSkills, 'junior');
  console.log('\nCareer Suggestions:');
  console.log(JSON.stringify(careers, null, 2));
}

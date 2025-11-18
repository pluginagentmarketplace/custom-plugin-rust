#!/usr/bin/env node

/**
 * Progress Tracker
 * Tracks user learning progress, analytics, and achievements
 */

class ProgressTracker {
  constructor() {
    this.userProgress = new Map();
    this.achievements = new Map();
    this.analytics = {
      totalUsersStarted: 0,
      totalAssessmentsCompleted: 0,
      averageScore: 0,
      mostPopularRoles: []
    };
  }

  /**
   * Initialize user progress
   */
  initializeUser(userId, role, level = 'beginner') {
    const userProgress = {
      userId: userId,
      role: role,
      level: level,
      startDate: new Date().toISOString(),
      progress: 0,
      completedTopics: [],
      assessmentScores: [],
      badges: [],
      certificates: [],
      lastActivity: new Date().toISOString()
    };

    this.userProgress.set(userId, userProgress);
    this.analytics.totalUsersStarted++;
    this.trackPopularRole(role);

    return userProgress;
  }

  /**
   * Update topic completion
   */
  completeTopicupdateTopic(userId, topic) {
    const progress = this.userProgress.get(userId);
    if (!progress) {
      throw new Error('User not found');
    }

    if (!progress.completedTopics.includes(topic)) {
      progress.completedTopics.push(topic);
      progress.progress = this.calculateProgress(progress.role, progress.completedTopics.length);
      progress.lastActivity = new Date().toISOString();

      // Check for milestones
      this.checkMilestones(userId, progress);
    }

    return progress;
  }

  /**
   * Record assessment score
   */
  recordAssessmentScore(userId, topic, score) {
    const progress = this.userProgress.get(userId);
    if (!progress) {
      throw new Error('User not found');
    }

    progress.assessmentScores.push({
      topic: topic,
      score: score,
      date: new Date().toISOString(),
      passed: score >= 75
    });

    this.analytics.totalAssessmentsCompleted++;
    this.updateAverageScore();

    // Award badge if score is high
    if (score >= 90) {
      this.awardBadge(userId, `master-${topic}`, 'Master');
    } else if (score >= 75) {
      this.awardBadge(userId, `intermediate-${topic}`, 'Intermediate');
    }

    progress.lastActivity = new Date().toISOString();

    return progress;
  }

  /**
   * Award badge
   */
  awardBadge(userId, badgeId, badgeName) {
    const progress = this.userProgress.get(userId);
    if (progress && !progress.badges.includes(badgeId)) {
      progress.badges.push(badgeId);

      // Trigger achievement
      this.trackAchievement(userId, `earned-badge-${badgeId}`, `Earned ${badgeName} Badge`);
    }
  }

  /**
   * Award certificate
   */
  awardCertificate(userId, role, level) {
    const progress = this.userProgress.get(userId);
    if (!progress) {
      throw new Error('User not found');
    }

    const certificate = {
      id: this.generateId(),
      role: role,
      level: level,
      issuedDate: new Date().toISOString(),
      expiryDate: new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toISOString(),
      verificationUrl: `https://custom-plugin-rust.verify/${certificate.id}`
    };

    progress.certificates.push(certificate);

    // Track achievement
    this.trackAchievement(userId, `certified-${role}`, `Completed ${role} Certification`);

    return certificate;
  }

  /**
   * Check for milestones
   */
  checkMilestones(userId, progress) {
    const topicCount = progress.completedTopics.length;
    const milestones = [
      { count: 5, achievement: 'milestone-5-topics', label: 'Completed 5 Topics' },
      { count: 10, achievement: 'milestone-10-topics', label: 'Completed 10 Topics' },
      { count: 20, achievement: 'milestone-20-topics', label: 'Completed 20 Topics' },
      { count: 50, achievement: 'completed-path', label: 'Completed Full Path' }
    ];

    milestones.forEach(m => {
      if (topicCount === m.count) {
        this.trackAchievement(userId, m.achievement, m.label);
      }
    });
  }

  /**
   * Track achievement
   */
  trackAchievement(userId, achievementId, label) {
    if (!this.achievements.has(userId)) {
      this.achievements.set(userId, []);
    }

    const userAchievements = this.achievements.get(userId);
    if (!userAchievements.find(a => a.id === achievementId)) {
      userAchievements.push({
        id: achievementId,
        label: label,
        unlockedDate: new Date().toISOString()
      });
    }
  }

  /**
   * Calculate progress percentage
   */
  calculateProgress(role, completedCount) {
    // Estimate total topics per role
    const totalTopicsPerRole = 20;
    return Math.min(100, Math.round((completedCount / totalTopicsPerRole) * 100));
  }

  /**
   * Track popular roles
   */
  trackPopularRole(role) {
    const existing = this.analytics.mostPopularRoles.find(r => r.role === role);
    if (existing) {
      existing.count++;
    } else {
      this.analytics.mostPopularRoles.push({ role: role, count: 1 });
    }

    this.analytics.mostPopularRoles.sort((a, b) => b.count - a.count);
    this.analytics.mostPopularRoles = this.analytics.mostPopularRoles.slice(0, 10);
  }

  /**
   * Update average score
   */
  updateAverageScore() {
    let totalScore = 0;
    let count = 0;

    this.userProgress.forEach(progress => {
      progress.assessmentScores.forEach(score => {
        totalScore += score.score;
        count++;
      });
    });

    this.analytics.averageScore = count > 0 ? Math.round(totalScore / count) : 0;
  }

  /**
   * Get user progress
   */
  getUserProgress(userId) {
    return this.userProgress.get(userId);
  }

  /**
   * Get user achievements
   */
  getUserAchievements(userId) {
    return this.achievements.get(userId) || [];
  }

  /**
   * Get leaderboard
   */
  getLeaderboard(limit = 10) {
    const leaderboard = Array.from(this.userProgress.values())
      .sort((a, b) => b.progress - a.progress)
      .slice(0, limit)
      .map((p, index) => ({
        rank: index + 1,
        userId: p.userId,
        role: p.role,
        progress: p.progress,
        badgeCount: p.badges.length,
        completedTopics: p.completedTopics.length
      }));

    return leaderboard;
  }

  /**
   * Get analytics
   */
  getAnalytics() {
    return {
      ...this.analytics,
      totalUsers: this.userProgress.size,
      topRoles: this.analytics.mostPopularRoles.slice(0, 5)
    };
  }

  /**
   * Generate unique ID
   */
  generateId() {
    return 'cert_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
  }
}

// Export for use in other modules
module.exports = ProgressTracker;

// If run directly
if (require.main === module) {
  const tracker = new ProgressTracker();

  // Example usage
  const userId = 'user123';
  tracker.initializeUser(userId, 'react', 'beginner');

  tracker.completeTopicupdateTopic(userId, 'JSX Basics');
  tracker.completeTopicupdateTopic(userId, 'Hooks');
  tracker.recordAssessmentScore(userId, 'react-basics', 85);

  console.log('User Progress:');
  console.log(JSON.stringify(tracker.getUserProgress(userId), null, 2));

  console.log('\nUser Achievements:');
  console.log(JSON.stringify(tracker.getUserAchievements(userId), null, 2));

  console.log('\nAnalytics:');
  console.log(JSON.stringify(tracker.getAnalytics(), null, 2));
}

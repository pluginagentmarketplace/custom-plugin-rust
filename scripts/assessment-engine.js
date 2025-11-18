#!/usr/bin/env node

/**
 * Assessment Engine
 * Creates and evaluates knowledge assessments for the learning system
 */

class AssessmentEngine {
  constructor() {
    this.assessments = new Map();
    this.results = new Map();
  }

  /**
   * Generate an assessment for a specific topic
   */
  generateAssessment(topic, difficulty = 'medium', questionCount = 10) {
    const assessment = {
      id: this.generateId(),
      topic: topic,
      difficulty: difficulty,
      questions: this.generateQuestions(topic, difficulty, questionCount),
      createdAt: new Date().toISOString(),
      timeLimit: difficulty === 'easy' ? 15 : difficulty === 'medium' ? 30 : 45
    };

    this.assessments.set(assessment.id, assessment);
    return assessment;
  }

  /**
   * Generate questions based on topic and difficulty
   */
  generateQuestions(topic, difficulty, count) {
    const questions = [];
    const questionBank = this.getQuestionBank(topic);

    const filtered = questionBank.filter(q => q.difficulty === difficulty);

    for (let i = 0; i < Math.min(count, filtered.length); i++) {
      questions.push({
        id: `q${i + 1}`,
        text: filtered[i].text,
        type: filtered[i].type,
        options: filtered[i].options,
        correctAnswer: filtered[i].correctAnswer
      });
    }

    return questions;
  }

  /**
   * Evaluate assessment answers
   */
  evaluateAssessment(assessmentId, answers) {
    const assessment = this.assessments.get(assessmentId);
    if (!assessment) {
      throw new Error('Assessment not found');
    }

    let correctCount = 0;
    const details = [];

    assessment.questions.forEach((question, index) => {
      const userAnswer = answers[`q${index + 1}`];
      const isCorrect = userAnswer === question.correctAnswer;

      if (isCorrect) correctCount++;

      details.push({
        questionId: question.id,
        userAnswer: userAnswer,
        correctAnswer: question.correctAnswer,
        isCorrect: isCorrect
      });
    });

    const score = Math.round((correctCount / assessment.questions.length) * 100);
    const passed = score >= 75;

    const result = {
      assessmentId: assessmentId,
      topic: assessment.topic,
      score: score,
      passed: passed,
      correctCount: correctCount,
      totalQuestions: assessment.questions.length,
      details: details,
      completedAt: new Date().toISOString(),
      nextSteps: this.getNextSteps(assessment.topic, passed, score)
    };

    this.results.set(assessmentId, result);
    return result;
  }

  /**
   * Get recommendations based on performance
   */
  getNextSteps(topic, passed, score) {
    if (!passed && score < 50) {
      return [
        `Review fundamentals of ${topic}`,
        `Take beginner-level practice questions`,
        `Watch tutorial videos on core concepts`,
        `Re-take assessment after revision`
      ];
    } else if (!passed && score < 75) {
      return [
        `Focus on weak areas in ${topic}`,
        `Practice with intermediate exercises`,
        `Review best practices`,
        `Re-take assessment`
      ];
    } else if (score >= 90) {
      return [
        `Congratulations! Master level achieved`,
        `Explore advanced topics in ${topic}`,
        `Consider mentoring others`,
        `Move to next specialization`
      ];
    } else {
      return [
        `Good progress! Continue learning`,
        `Explore advanced concepts in ${topic}`,
        `Work on real-world projects`,
        `Consider next skill area`
      ];
    }
  }

  /**
   * Get question bank for a topic
   */
  getQuestionBank(topic) {
    const banks = {
      'javascript': [
        {
          text: 'What is the difference between let and var?',
          type: 'multiple-choice',
          options: ['Scope and hoisting', 'Performance', 'Browser support', 'None'],
          correctAnswer: 'Scope and hoisting',
          difficulty: 'easy'
        },
        {
          text: 'Explain closure in JavaScript',
          type: 'short-answer',
          options: [],
          correctAnswer: 'A function that has access to variables from its outer scope',
          difficulty: 'medium'
        },
        {
          text: 'What are Promises and async/await?',
          type: 'multiple-choice',
          options: ['Error handling', 'Asynchronous operations', 'Callbacks', 'All of the above'],
          correctAnswer: 'Asynchronous operations',
          difficulty: 'medium'
        }
      ],
      'react': [
        {
          text: 'What is the purpose of the useEffect hook?',
          type: 'multiple-choice',
          options: ['Render components', 'Handle side effects', 'Manage state', 'Create context'],
          correctAnswer: 'Handle side effects',
          difficulty: 'easy'
        },
        {
          text: 'Explain React functional components vs class components',
          type: 'short-answer',
          options: [],
          correctAnswer: 'Functional components use hooks, class components use lifecycle methods',
          difficulty: 'medium'
        }
      ],
      'python': [
        {
          text: 'What is a Python decorator?',
          type: 'multiple-choice',
          options: ['A design pattern', 'A function modifier', 'A class inheritance', 'An import statement'],
          correctAnswer: 'A function modifier',
          difficulty: 'medium'
        },
        {
          text: 'Difference between list and tuple?',
          type: 'multiple-choice',
          options: ['Lists are mutable, tuples are immutable', 'Tuples are mutable', 'No difference', 'Lists are immutable'],
          correctAnswer: 'Lists are mutable, tuples are immutable',
          difficulty: 'easy'
        }
      ],
      'sql': [
        {
          text: 'What is a JOIN in SQL?',
          type: 'multiple-choice',
          options: ['Combine rows from different tables', 'Delete records', 'Update data', 'Create indexes'],
          correctAnswer: 'Combine rows from different tables',
          difficulty: 'easy'
        },
        {
          text: 'Difference between INNER, LEFT, and FULL JOIN?',
          type: 'short-answer',
          options: [],
          correctAnswer: 'INNER returns matching rows, LEFT keeps all left table rows, FULL keeps all rows',
          difficulty: 'medium'
        }
      ]
    };

    // Default question bank if topic not found
    const defaultBank = [
      {
        text: `What is the basic concept of ${topic}?`,
        type: 'multiple-choice',
        options: ['Option A', 'Option B', 'Option C', 'Option D'],
        correctAnswer: 'Option A',
        difficulty: 'easy'
      },
      {
        text: `Advanced topic in ${topic}?`,
        type: 'multiple-choice',
        options: ['Option A', 'Option B', 'Option C', 'Option D'],
        correctAnswer: 'Option B',
        difficulty: 'medium'
      },
      {
        text: `Expert level question about ${topic}?`,
        type: 'short-answer',
        options: [],
        correctAnswer: 'Expert answer',
        difficulty: 'hard'
      }
    ];

    return banks[topic] || defaultBank;
  }

  /**
   * Generate unique ID
   */
  generateId() {
    return 'assessment_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
  }

  /**
   * Get assessment result
   */
  getResult(assessmentId) {
    return this.results.get(assessmentId);
  }
}

// Export for use in other modules
module.exports = AssessmentEngine;

// If run directly
if (require.main === module) {
  const engine = new AssessmentEngine();

  // Example usage
  const assessment = engine.generateAssessment('javascript', 'medium', 3);
  console.log('Generated Assessment:');
  console.log(JSON.stringify(assessment, null, 2));

  // Simulate user answers
  const answers = {
    q1: 'Scope and hoisting',
    q2: 'A function that has access to variables from its outer scope',
    q3: 'Asynchronous operations'
  };

  const result = engine.evaluateAssessment(assessment.id, answers);
  console.log('\nAssessment Result:');
  console.log(JSON.stringify(result, null, 2));
}

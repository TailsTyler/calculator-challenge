// /** @type {import('ts-jest').JestConfigWithTsJest} */
// module.exports = {
//   preset: 'ts-jest',
//   testEnvironment: 'node',
// };

// /** @type {import('ts-jest').JestConfigWithTsJest} */
// module.exports = {
//   //preset: 'ts-jest',
//   preset: 'jest-preset-angular',
//   setupFilesAfterEnv: ['<rootDir>/setup-jest.ts'],
//   testEnvironment: 'jsdom', // or 'node' if no DOM is needed
//   transform: {
//     '^.+\\.tsx?$': 'ts-jest',
//     '^.+\\.mjs$': 'ts-jest', // <- add this to handle Angular's .mjs
//   },
//   moduleFileExtensions: ['ts', 'html', 'js', 'json', 'tsx', 'jsx', 'json', 'node', 'mjs'],
//   transformIgnorePatterns: [
//     'node_modules/(?!@angular|rxjs)' // <- allow transforming Angular packages
//   ],
// };
/** @type {import('ts-jest').JestConfigWithTsJest} */
module.exports = {
  preset: 'jest-preset-angular',
  setupFilesAfterEnv: ['<rootDir>/setup-jest.ts'],
  testEnvironment: 'jsdom',

  transform: {
    '^.+\\.(ts|mjs|html)$': 'ts-jest',
  },

  transformIgnorePatterns: [
    'node_modules/(?!@angular|rxjs)',
  ],

  moduleFileExtensions: ['ts', 'html', 'js', 'json', 'mjs'],
};

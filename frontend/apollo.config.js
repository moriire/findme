'use strict'
/* eslint-env node */
// See https://www.apollographql.com/docs/devtools/apollo-config/
module.exports = {
  client: {
    service: {
      name: 'findme-service',
      url: 'http://127.0.0.1:8000/graphql',
      skipSSLValidation: true,
    },
    // Files processed by the extension
    includes: ['src/**/*.vue', 'src/**/*.js', 'src/**/*.ts'],
  },
}
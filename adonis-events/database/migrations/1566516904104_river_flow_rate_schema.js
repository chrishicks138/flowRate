'use strict'

/** @type {import('@adonisjs/lucid/src/Schema')} */
const Schema = use('Schema')

class RiverFlowRateSchema extends Schema {
  up () {
    this.create('river_flow_rates', (table) => {
      table.increments()
      table.string('flowrate').nullable()
      table.timestamps()
    })
  }

  down () {
    this.drop('river_flow_rates')
  }
}

module.exports = RiverFlowRateSchema

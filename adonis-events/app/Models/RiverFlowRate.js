'use strict'

/** @type {typeof import('@adonisjs/lucid/src/Lucid/Model')} */
const Model = use('Model')

class RiverFlowRate extends Model {
  static get table () {
    return 'river_flow_rates'
  }
  static get primaryKey () {
     return 'site'
  }
}

module.exports = RiverFlowRate

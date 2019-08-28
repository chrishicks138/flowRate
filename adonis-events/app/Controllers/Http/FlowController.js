///RiverFlowRate = RiverFlowRate
///river_flow_rates = river_flow_rates
///flowRate = flowRate

'use strict'
const RiverFlowRate = use('App/Models/RiverFlowRate')
class FlowController {
  async index ({response}) {
    let river_flow_rates = await RiverFlowRate.all()
    return response.json(river_flow_rates)
  }

  async show ({params, response}) {
    let flowRate = await RiverFlowRate.find(params.site)
    if (!flowRate) {
      return response.status(404).json({data: 'Resource not found'})
    }
    return response.status(200).json(flowRate.flowrate)
  }

  async showall ({params, response}) {
    const flowRate = await RiverFlowRate.find(params.site)
    return response.status(200).json(flowRate)
  }

  async store ({request, response}) {
    const flowRateInfo = request.only(['site','flowrate','date','timezone'])
    const flowRate = new RiverFlowRate()
    flowRate.flowrate = flowRateInfo.flowrate
    flowRate.site = flowRateInfo.site
    flowRate.date = flowRateInfo.date
    flowRate.timezone = flowRateInfo.timezone
    await flowRate.save()
    return response.status(201).json(flowRate)
  }

  async update ({params, request, response}) {
    const flowRateInfo = request.only(['site','flowrate','date','timezone'])
    const flowRate = await RiverFlowRate.find(params.site)
    if (!flowRate) {
      return response.status(404).json({data: 'Resource not found'})
    }
    flowRate.flowrate = flowRateInfo.flowrate
    flowRate.site = flowRateInfo.site
    flowRate.date = flowRateInfo.date
    flowRate.timezone = flowRateInfo.timezone
    await flowRate.save()
    return response.status(200).json(flowRate)
  }

  async delete ({params, response}) {
    const flowRate = await RiverFlowRate.find(params.id)
    if (!flowRate) {
      return response.status(404).json({data: 'Resource not found'})
    }
    await flowRate.delete()
    return response.status(204).json(null)
  }

  async current ({response}) {
    let current = await RiverFlowRate.getMax('id')
    const flowRate = await RiverFlowRate.find(current)
    return response.json(flowRate.flowRate+'\n')
  }

}

module.exports = FlowController

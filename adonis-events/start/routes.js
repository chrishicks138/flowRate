    
///RiverFlowRate = RiverFlowRate
///flowRate = flowRate
///river_flow_rates = river_flow_rates
'use strict'
const Route = use('Route')
const RiverFlowRate = use('App/Models/RiverFlowRate')
Route.group(() => {
  Route.post('river_flow_rates', async ({ request, response }) => {
    const flowRateInfo = request.only(['flowrate'])
    const flowRate = new RiverFlowRate()
    flowRate.flowrate = flowRateInfo.flowrate
    await flowRate.save()
    return response.status(201).json(flowRate)
  })
  Route.get('river_flow_rates', async ({ response }) => {
    let river_flow_rates = await RiverFlowRate.all()
    return response.json(river_flow_rates)
  })
  Route.get('river_flow_rates/:id', async ({ params, response }) => {
    const flowRate = await RiverFlowRate.find(params.id)
    return response.json(flowRate)
  })
  Route.put('river_flow_rates/:id', async ({ params, request, response }) => {
    const flowRateInfo = request.only(['flowrate'])
    const flowRate = await RiverFlowRate.find(params.id)
    flowRate.flowrate = flowRateInfo.flowrate
    await flowRate.save()
    return response.status(200).json(flowRate)
  })
  Route.delete('river_flow_rates/:id', async ({ params, response }) => {
    const flowRate = await RiverFlowRate.find(params.id)
    if (!flowRate) {
      return response.status(404).json(null)
    }yy
    await flowRate.delete()
    return response.status(204).json(null)
  })
  Route.get('current', async ({ response }) => {
    let current = await RiverFlowRate.getMax('id')
    const flowRate = await RiverFlowRate.find(current)
    return response.json(flowRate.flowrate)
  })
}).prefix('api/13206000')
///await User.pickInverse() 

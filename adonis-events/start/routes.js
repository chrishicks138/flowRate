const Route = use('Route')
    Route.group(() => {
      Route.post('river_flow_rates', 'FlowController.store')
      Route.get('river_flow_rates', 'FlowController.index')
      Route.get(':site', 'FlowController.show')
      Route.get(':site/all', 'FlowController.showall')
      Route.put('update/:site', 'FlowController.update')
      Route.delete('river_flow_rates/:id', 'FlowController.delete')
    }).prefix('api/')

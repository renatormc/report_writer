export type WidgetAttributesType = {
    widget_props: any,
    field_name: string,
    widget_type: string,
    label: string,
    col: number
}

export type WidgetMatrixType = Array<Array<WidgetAttributesType>>

export type ErrorsType = { [key: string]: any }

export type DataType  = { [key: string]: any }
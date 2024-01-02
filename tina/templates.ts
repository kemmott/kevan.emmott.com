import type { TinaField } from "tinacms";
export function pageFields() {
  return [
    {
      type: "string",
      name: "layout",
      label: "layout",
    },
    {
      type: "string",
      name: "title",
      label: "title",
    },
    {
      type: "string",
      name: "permalink",
      label: "permalink",
    },
  ] as TinaField[];
}
export function postFields() {
  return [
    {
      type: "string",
      name: "layout",
      label: "layout",
    },
    {
      type: "string",
      name: "title",
      label: "title",
    },
    {
      type: "datetime",
      name: "date",
      label: "date",
    },
    {
      type: "object",
      name: "author",
      label: "author",
      fields: [
        {
          type: "string",
          name: "display_name",
          label: "display_name",
        },
      ],
    },
  ] as TinaField[];
}
